from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('list/', views.score_list, name='list'),
    path('learning/', views.learning, name='learning'),
    
    path('score/score_id=<int:score_id>/', views.specific_score, name='specific_score'),
    path('add_score/', views.add_score, name='add_score'),
    path('add_feedback_to_score/', views.add_feedback_to_score, name='add_feedback_to_score'),
]