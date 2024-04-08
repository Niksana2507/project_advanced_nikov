# Generated by Django 5.0.3 on 2024-04-08 14:27

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_appuser_options_remove_appuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'Потребител с това име вече съществува!'}, help_text='Използвайте букви, цифри и @/./+/-/_ . Не повече от 150 символа!', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='потребител'),
        ),
    ]