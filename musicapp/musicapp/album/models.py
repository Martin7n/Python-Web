from django.core.validators import MinValueValidator
from django.db import models

from musicapp.user_profile.models import Profile


# Create your models here.

class Album (models.Model):
    MAX_LEN_ALBUM_NAME = 30
    MAX_LEN_ARTIST_NAME = 30
    MIN_LEN_GENRE = 30

    GENRES = ["Pop Music", "Jazz Music", "R&B Music",
              "Rock Music", "Country Music", "Dance Music",
              "Hip Hop Music", "Other"]
    CHOICES = tuple([(c, c) for c in GENRES])

    album_name = models.CharField(
        max_length=MAX_LEN_ALBUM_NAME,
        unique=True,
        blank=False,
        null=False,
    )
    artist = models.CharField(
        max_length=MAX_LEN_ARTIST_NAME,
        blank=False,
        null=False,
    )
    genre = models.CharField(
        max_length=MIN_LEN_GENRE,
        blank=False,
        null=False,
        choices=CHOICES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    album_picture_url = models.URLField(
        blank=False,
        null=False,)

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0.0), ]
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,
                              related_name='albums')
