from django import forms

from project_advanced_nikov.cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'engine_type', 'year', 'vin', 'description']
        labels = {
            'model': 'Модел',
            'engine_type': 'Двигател',
            'year': 'Година',
            'vin': 'VIN',
            'description': 'Описание',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
