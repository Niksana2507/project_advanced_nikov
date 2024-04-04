from django.urls import path

from project_advanced_nikov.accounts.views import AppUserRegister, LoginAppUserView, LogoutAppUserView

urlpatterns = (
    path("register/", AppUserRegister.as_view(), name="register"),
    path("login/", LoginAppUserView.as_view(), name="login"),
    path("logout/", LogoutAppUserView.as_view(), name="logout"),
)