from django.contrib import admin

from musicapp.album.models import Album
from musicapp.user_profile.models import Profile


# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        "album_name",
        "artist",
        "genre",
        "description",
        "album_picture_url",
        "price",
        "owner",
    ]
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "age",
    ]
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    #