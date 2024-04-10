from django.contrib import admin

from project_advanced_nikov.cars.models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'model', 'engine_type', 'year', 'vin', 'user',)
    search_fields = ('user__username', 'model', 'engine_type',)
    ordering = ('pk',)