from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/<str:level>/<int:question_id>/', views.quiz, name='quiz'),
    path('result/<str:level>/<int:level_number>/', views.result, name='result'),

]
