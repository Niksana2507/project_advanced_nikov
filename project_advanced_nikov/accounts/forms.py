from django import forms
from django.contrib.auth.forms import BaseUserCreationForm

from project_advanced_nikov.accounts.models import AppUser, Profile


class AppUserForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = AppUser
        fields = ("username", "email")

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ("user",)