from django.urls import path

from project_advanced_nikov.accounts.views import AppUserRegister, LoginAppUserView, LogoutAppUserView, \
    ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path("register/", AppUserRegister.as_view(), name="register"),
    path("login/", LoginAppUserView.as_view(), name="login"),
    path("logout/", LogoutAppUserView.as_view(), name="logout"),
    path("profile/<int:pk>/", ProfileDetailsView.as_view(), name="profile"),
    path("profile/<int:pk>/edit/", ProfileEditView.as_view(), name="edit"),
    path("profile/<int:pk>/delete/", ProfileDeleteView.as_view(), name="delete"),

)