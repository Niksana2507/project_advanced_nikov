from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from project_advanced_nikov.accounts.forms import AppUserForm, ProfileForm, RegisterForm
from project_advanced_nikov.accounts.mixins import CustomLoginRequiredMixin
from project_advanced_nikov.accounts.models import AppUser, Profile


# Create your views here.
class AppUserRegister(CreateView):
    model = AppUser
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")


class LoginAppUserView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("index")


class LogoutAppUserView(LogoutView):
    pass

class ProfileDetailsView(CustomLoginRequiredMixin, DetailView):
    template_name = "accounts/profile.html"
    model = Profile

class ProfileEditView(CustomLoginRequiredMixin, UpdateView):
    template_name = "accounts/edit.html"
    model = Profile
    form_class = ProfileForm
    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk":self.object.pk})

class ProfileDeleteView(CustomLoginRequiredMixin, DeleteView):
    template_name = "accounts/delete.html"
    model = Profile
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        self.request.user.delete()
        return super().form_valid(form)
