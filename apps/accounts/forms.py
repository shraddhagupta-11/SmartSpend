from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "phone_number",
            "password1",
            "password2",
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "phone_number",
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "profile_picture",
            "bio",
        )