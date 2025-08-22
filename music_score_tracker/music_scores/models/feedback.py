from django.db import models
from django.contrib.auth.models import User
from music_scores.models import Score
from music_scores.enums import ScoreSignatures, ScoreDifficulty, ScoreInstrument
from enum import Enum
from django.core.validators import MinValueValidator, MaxValueValidator

class Feedback(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE, related_name='feedback')
