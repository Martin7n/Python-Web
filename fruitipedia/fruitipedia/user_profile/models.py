from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.commoms.validators import first_letter_validator


# Create your models here.

class Profile(models.Model):


    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), first_letter_validator])

    #todo first=letter or ValidationError "Your name must start with a letter!"
    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1), first_letter_validator])
    # todo first=letter or ValidationError "Your name must start with a letter!"
    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False,
        unique=True)
    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[MinLengthValidator(8)])
    #TODO min_length - 8 (with help text)
    #TODO  HELP TEXT "*Password length requirements: 8 to 20 characters"
    profile_picture = models.URLField(
        blank=True,
        null=True)

    age = models.PositiveIntegerField(
        default=18,
        blank=True,
        null=False)
