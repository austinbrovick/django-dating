from django import forms

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "gender",
            "seeking",
            "github_username",
            "favorite_programming_language",
            "profile_picture",
            "college",
            "current_title",
            "current_employer",
            "race",
        ]

