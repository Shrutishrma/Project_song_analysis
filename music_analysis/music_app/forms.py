# music_analysis/forms.py
from django import forms

class RecommendationForm(forms.Form):
    genres = forms.CharField(max_length=100, required=False)
    duration_in_min = forms.FloatField(required=False)
    release_year = forms.IntegerField(required=False)
