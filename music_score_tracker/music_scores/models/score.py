from django.db import models
from django.contrib.auth.models import User
from music_scores.enums import ScoreSignatures, ScoreDifficulty, ScoreInstrument
from enum import Enum

# Create your models here.


class Score(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    signature = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in ScoreSignatures], default=ScoreSignatures.FOURFOUR.value)
    difficulty = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in ScoreDifficulty], default=ScoreDifficulty.INTERMEDIATE.value)
    instrument = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in ScoreInstrument], default=ScoreInstrument.PIANO.value)
    measure_count = models.IntegerField(default=10, max_length=500)
    beats_per_minute = models.IntegerField(default=1,  max_length=250)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} | {self.difficulty} | {self.instrument} | {self.instrument} | measures: {self.measure_count} | BPM: {self.beats_per_minute}'