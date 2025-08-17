from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Score

# Create your views here.
@login_required
def welcome(request):
    return render(request, 'pages/welcome.html', {'scores': [Score(title='Tanz'), Score(title='Mazurka')]})

@login_required
def score_list(request):
    return render(request, 'pages/score_list.html', {'scores': [Score(title='Tanz'), Score(title='Mazurka')]})


@login_required
def learning(request):
    return render(request, 'pages/learning.html')