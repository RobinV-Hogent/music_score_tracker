from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('list/', views.score_list, name='score_list'),
]