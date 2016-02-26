from django import forms

from .models import Algo

class AlgoForm(forms.ModelForm):
    class Meta:
        model = Algo
        fields = [
            "algorithm",
            "answer",
        ]
