from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('list/', views.score_list, name='list'),
    path('learning/', views.learning, name='learning'),
]