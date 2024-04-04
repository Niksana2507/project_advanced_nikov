from django.contrib.auth.forms import BaseUserCreationForm

from project_advanced_nikov.accounts.models import AppUser


class AppUserForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = AppUser
        fields = ("username", "email")
