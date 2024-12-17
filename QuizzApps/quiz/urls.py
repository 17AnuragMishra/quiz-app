from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('get-question/', views.get_question, name='get_question'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),
    path('end-quiz/', views.end_quiz, name='end_quiz'),
    path('results/', views.results, name='quiz_results'), 
]
