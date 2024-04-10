from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from project_advanced_nikov.accounts.forms import RegisterForm, AppUserChangeForm
from project_advanced_nikov.accounts.models import AppUser


# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    model = AppUser
    add_form = RegisterForm
    form = AppUserChangeForm

    list_display = ('pk', 'username', 'email', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username',)
    ordering = ('pk',)

    fieldsets = ((None, {'fields': ('username', 'password')}),
                 ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
                 ('Important dates', {'fields': ('last_login', "date_joined")}),)

    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("username", "email", "password1", "password2"), },),)
