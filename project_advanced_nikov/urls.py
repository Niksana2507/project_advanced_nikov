from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('project_advanced_nikov.web.urls')),
    path("account/", include('project_advanced_nikov.accounts.urls'))
    # path("nachalo/", include('project_advanced_nikov.web.urls')),

]
