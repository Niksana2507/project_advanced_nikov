from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm

from project_advanced_nikov.accounts.models import AppUser, Profile


class AppUserForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = AppUser
        fields = ("username", "email")

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ("user",)

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Парола', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторете паролата', widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролите не съвпадат!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = AppUser