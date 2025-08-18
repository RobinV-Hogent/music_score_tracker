from django import forms
from ..models import Score

class ScoreCreateForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ["title", "signature", "difficulty", "instrument", "measure_count", "beats_per_minute"]