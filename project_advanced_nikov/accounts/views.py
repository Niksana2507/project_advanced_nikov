from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from project_advanced_nikov.accounts.forms import AppUserForm
from project_advanced_nikov.accounts.models import AppUser


# Create your views here.
class AppUserRegister(CreateView):
    model = AppUser
    template_name = "accounts/register.html"
    form_class = AppUserForm
    success_url = reverse_lazy("login")


class LoginAppUserView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("index")


class LogoutAppUserView(LogoutView):
    pass