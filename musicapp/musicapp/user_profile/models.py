from django.core.validators import MinLengthValidator
from django.db import models

from musicapp.core import custom_validators


class Profile(models.Model):

    MAX_NAME_VALUE = 15
    MIN_NAME_VALUE = 2

    username = models.CharField(
        max_length=MAX_NAME_VALUE,
        null=False,
        blank=False,
        validators=[MinLengthValidator(MIN_NAME_VALUE),  custom_validators.alphabet_validator])

    # TODO- DONE!
    # raise a ValidationError with the message: "Ensure this value contains only letters, numbers, and underscore."

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False,
        unique=True)

    age = models.PositiveIntegerField(
        blank=True,
        null=False)
    # todo The age cannot be below 0.
    # password = models.CharField(
    #     max_length=20,
    #     null=False,
    #     blank=False,
    #     validators=[MinLengthValidator(8)])
    # #TODO min_length - 8 (with help text)
    # #TODO  HELP TEXT "*Password length requirements: 8 to 20 characters"
    # profile_picture = models.URLField(
    #     blank=True,
    #     null=True)
