from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Car(models.Model):
    class CarModel(models.TextChoices):
        BMW = "BMW"
        MERCEDES = "Mercedes"
        VW = "Volkswagen"
        PEUGEOT = "Peugeot"
        OPEL = "OPEL"
        OTHER = "Other"

    class EngineType(models.TextChoices):
        DIESEL = "Дизел"
        PETROL = "Бензин"
        HYBRID = "Хибрид"

    MAX_LENGTH = 10
    MAX_VIN_LENGTH = 17
    MAX_DESCRIPTION_LENGTH = 500

    model = models.CharField(
        max_length=MAX_LENGTH,
        choices=CarModel.choices,
        null=False,
        blank=False,
    )

    engine_type = models.CharField(
        max_length=MAX_LENGTH,
        choices=EngineType.choices,
        null=False,
        blank=False,
    )

    year = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    vin = models.CharField(
        max_length=MAX_VIN_LENGTH,
        null=False,
        blank=False,
        validators=[MinLengthValidator(17)],
        unique=True,
        error_messages={'unique': "Този VIN номер вече се използва! Опитайте отново!"},
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
    )
