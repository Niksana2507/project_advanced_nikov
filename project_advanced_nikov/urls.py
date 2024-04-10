from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('project_advanced_nikov.web.urls')),
    path("accounts/", include('project_advanced_nikov.accounts.urls')),
    path("cars/", include('project_advanced_nikov.cars.urls')),

]
