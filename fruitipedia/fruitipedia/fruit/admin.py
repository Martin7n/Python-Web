from django.contrib import admin

from fruitipedia.fruit.models import Fruit
from fruitipedia.user_profile.models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', "email", "password", "profile_picture", "age"]
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ["fruit_name", "fruit_image_url", "description", "nutrition", "owner"]
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    #

