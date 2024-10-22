from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from worldofspeed.user_profile.models import Profile

from worldofspeed.core import custom_validators
# Create your models here.

class Car(models.Model):
    MAX_CARTYPE = 10
    MAX_MODEL = 15
    MIN_MODEL = 1
    MAX_LEN_ALBUM_NAME = 30
    MAX_LEN_ARTIST_NAME = 30
    MIN_LEN_GENRE = 30

    CAR_TYPES = ["Rally", "Open-wheel", "Kart", "Drag", "Other"]
    CHOICES = tuple([(c, c) for c in CAR_TYPES])

    car_model = models.CharField(
        max_length=MAX_MODEL,
        validators=[MinLengthValidator(MIN_MODEL)],
        blank=False,
        null=False)

    car_type = models.CharField(
        max_length=MAX_CARTYPE,
        blank=False,
        null=False,
        choices=CHOICES
    )

    year = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[custom_validators.year_validator]
    )

    car_picture = models.URLField(
        blank=False,
        null=False,
        unique=True,
        error_messages={"unique":"This image URL is already in use! Provide a new one."}
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1.0), ]
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,
                              related_name='cars')
