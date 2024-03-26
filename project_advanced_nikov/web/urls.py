from django.urls import path
from project_advanced_nikov.web.views import index

urlpatterns = (
    path("", index, name="index"),
    # path("nachalo/", nachalo, name="nachalo"),
)