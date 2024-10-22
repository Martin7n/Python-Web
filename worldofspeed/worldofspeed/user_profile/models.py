from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldofspeed.core import custom_validators


class Profile(models.Model):

    MAX_USERNAME_VALUE = 15
    MIN_MAX_USERNAME_VALUE_VALUE = 3
    MIN_AGE = 21
    MIN_NAME = 0
    MAX_NAME = 25

    username = models.CharField(
        max_length=MAX_USERNAME_VALUE,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_MAX_USERNAME_VALUE_VALUE),
            custom_validators.alphabet_validator],
        )

    email = models.EmailField(
        blank=False,
        null=False)

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(MIN_AGE),])

    password = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        help_text="Age requirement: 21 years and above.")


    first_name = models.CharField(
        max_length=MAX_NAME,
        blank=True,
        null=True)

    last_name = models.CharField(
        max_length=MAX_NAME,
        blank=True,
        null=True)

    profile_picture = models.URLField(
        blank=False,
        null=False,)

