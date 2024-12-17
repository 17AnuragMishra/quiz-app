from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Question, Option, UserAnswer
import random
import json


@login_required
def start_quiz(request):
    UserAnswer.objects.filter(user=request.user).delete()
    request.session["current_question"] = 0
    return render(request, 'quiz/start.html')


@login_required
def get_question(request):
    answered_questions = UserAnswer.objects.filter(user=request.user).values_list('question_id', flat=True)
    question = Question.objects.exclude(id__in=answered_questions).order_by("?").first()
    if question:
        options = [{"id": opt.id, "text": opt.option_text} for opt in question.options.all()]
        return JsonResponse({
            "id": question.id,
            "question": question.question_text,
            "options": options
        })

    return JsonResponse({"end": True})


@login_required
def submit_answer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        question_id = data.get("question_id")
        selected_option_id = data.get("option_id")

        question = Question.objects.get(id=question_id)
        selected_option = Option.objects.get(id=selected_option_id)
        is_correct = selected_option.is_correct
        UserAnswer.objects.create(
            user=request.user,
            question=question,
            selected_option=selected_option,
            is_correct=is_correct
        )

       
        correct_answers = UserAnswer.objects.filter(user=request.user, is_correct=True).count()
        incorrect_answers = UserAnswer.objects.filter(user=request.user, is_correct=False).count()

        return JsonResponse({
            "result": "Correct" if is_correct else "Incorrect",
            "correct_answers": correct_answers,
            "incorrect_answers": incorrect_answers,
            "questions_answered": UserAnswer.objects.filter(user=request.user).count(),
        })


@login_required
def end_quiz(request):
    total_questions = UserAnswer.objects.filter(user=request.user).count()
    correct_answers = UserAnswer.objects.filter(user=request.user, is_correct=True).count()
    incorrect_answers = total_questions - correct_answers

    return JsonResponse({
        'message': 'Quiz Completed!',
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
    })


@login_required
def results(request):
    answers = UserAnswer.objects.filter(user=request.user).select_related('question', 'selected_option')

    results_data = [
        {
            "question": ans.question.question_text,
            "selected_option": ans.selected_option.option_text,
            "is_correct": ans.is_correct
        } for ans in answers
    ]

    return JsonResponse({"results": results_data})


def home(request):
    return render(request, 'quiz/home.html')
