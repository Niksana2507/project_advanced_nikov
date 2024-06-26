from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("потребител"),
        max_length=150,
        unique=True,
        help_text=_(
            "Използвайте букви, цифри и @/./+/-/_ . Не повече от 150 символа!"
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Потребител с това име вече съществува!"),
        },
    )

    email = models.EmailField(_("email"), blank=False, null=False, unique=True)

    is_staff = models.BooleanField(default=False, )

    is_active = models.BooleanField(default=True, )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "username"

    objects = UserManager()

class Profile(models.Model):
    age = models.IntegerField(
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete= models.CASCADE,
        primary_key=True,
    )