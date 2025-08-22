from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from music_scores.models import Score, Feedback
from .forms import ScoreCreateForm

# Create your views here.
@login_required
def welcome(request):
    
    if request.method == 'POST':
        form = ScoreCreateForm(request.POST)
        score_form_helper(request, form, 'welcome')
    
    scores = Score.objects.filter(user=request.user)
    form = ScoreCreateForm()
    
    
    return render(request, 'pages/welcome.html', {'scores': scores, 'form': form})


@login_required
def add_score(request):
    """
    Page with form that allows the user to add new scores
    """
    
    if request.method == "POST":
        form = ScoreCreateForm(request.POST)
        return score_form_helper(request, form, 'welcome')  # redirect after success
    else:
        form = ScoreCreateForm()

    return render(request, "pages/create_score.html", {"form": form})


def score_form_helper(request, form, page):
    if form.is_valid():
        score: Score = form.save(commit=False)
        score.user = request.user   # attach logged-in user
        score.save()
        return redirect(page)
    

@login_required
def score_list(request):
    return render(request, 'pages/score_list.html', {'scores': Score.objects.all()})


@login_required
def learning(request):
    return render(request, 'pages/learning.html')


@login_required
def specific_score(request, score_id:int):
    """
    Renders the page of a specific score
    This page shows the properties of this score
    Feedback should also be shown here
    Users can add feedback to the score
    """
    
    
    score = get_object_or_404(Score, id=score_id, user=request.user)
    
    f1 = Feedback.objects.create(score=score, content='Get better', user=request.user) 
    
    score = get_object_or_404(Score, id=score_id, user=request.user)
    
    return render(request, 'pages/specific_score.html', {"score": score, "feedback": score.feedback.all()})
   
    

@login_required
def add_feedback_to_score(request):
    """
    Adds feedback to a specific score
    This will send the user back to the page of the score they had initially clicked on
    """
    
    # Add feedback to the current score.
    # Send the user back to the specific score page 
    
    return render(request, '<p>Test</p>')