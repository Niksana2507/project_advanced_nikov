from django.urls import path
from project_advanced_nikov.web.views import index, forus, services, contact

urlpatterns = (
    path("", index, name="index"),
    path("forus/", forus, name="forus"),
    path("services/", services, name="services"),
    path("contact/", contact, name="contact"),
)