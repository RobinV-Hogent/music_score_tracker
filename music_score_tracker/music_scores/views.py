from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Score
from .forms import ScoreCreateForm

# Create your views here.
@login_required
def welcome(request):
    return render(request, 'pages/welcome.html', {'scores': Score.objects.all()})

@login_required
def score_list(request):
    return render(request, 'pages/score_list.html', {'scores': [Score(title='Tanz'), Score(title='Mazurka')]})


@login_required
def learning(request):
    return render(request, 'pages/learning.html')


@login_required
def specific_score(request):
    """
    Renders the page of a specific score
    This page shows the properties of this score
    Feedback should also be shown here
    Users can add feedback to the score
    """
    
    return render(request, '<h1>Score Page</h1>')


@login_required
def add_score(request):
    """
    Page with form that allows the user to add new forms
    """
    
    if request.method == "POST":
        form = ScoreCreateForm(request.POST)
        if form.is_valid():
            score: Score = form.save(commit=False)
            score.user = request.user   # attach logged-in user
            score.save()
            return redirect("welcome")  # redirect after success
    else:
        form = ScoreCreateForm()

    return render(request, "pages/create_score.html", {"form": form})
    
    

@login_required
def add_feedback_to_score(request):
    """
    Adds feedback to a specific score
    This will send the user back to the page of the score they had initially clicked on
    """
    
    # Add feedback to the current score.
    # Send the user back to the specific score page 
    
    return render(request, '<p>Test</p>')