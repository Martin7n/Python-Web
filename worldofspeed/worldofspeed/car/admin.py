from django.contrib import admin

from worldofspeed.car.models import Car
from worldofspeed.user_profile.models import Profile


# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "car_model",
        "car_type",
        "year",
        "car_picture",
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
        "password",
        "first_name",
        "last_name",
        "profile_picture",
    ]
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    #