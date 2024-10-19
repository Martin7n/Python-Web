from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.commoms.validators import first_letter_validator, only_letters
from fruitipedia.user_profile.models import Profile


# Create your models here.

class Fruit(models.Model):


    fruit_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
        validators=[MinLengthValidator(2), first_letter_validator, only_letters])

    fruit_image_url = models.URLField(
        blank=False,
        null=False)

    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Profile,
        models.CASCADE,
        blank=True,
        null=False)
