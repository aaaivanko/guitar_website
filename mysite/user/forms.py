from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadUserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UploadUserPhoto(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'guitar_model']