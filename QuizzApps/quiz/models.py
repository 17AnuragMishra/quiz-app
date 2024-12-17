from django.db import models
from django.contrib.auth.models import User  # To associate answers with users

class Question(models.Model):
    question_text = models.CharField(max_length=255, default="No Question Text")
    def __str__(self):
        return self.question_text


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text


# New Model for User Submissions
class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"User: {self.user.username} | Question: {self.question} | Correct: {self.is_correct}"
