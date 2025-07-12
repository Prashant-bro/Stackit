from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questions/', views.question_list, name='question_list'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('api/questions/', views.create_question_api, name='create_question_api'),
] 