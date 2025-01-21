from django import forms
from .models import UserScore

class UserScoreForm(forms.ModelForm):
    class Meta:
        model = UserScore
        fields = ['username', 'xp_points'] 