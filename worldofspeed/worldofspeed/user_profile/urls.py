from django.shortcuts import render
from django.urls import path, include

from worldofspeed.user_profile.views import create_profile, delete_profile, profile_details, edit_profile

# Create your views here.



urlpatterns = [
    path("edit/", edit_profile, name="edit-profile"),
    path('delete/', delete_profile, name='delete-profile'),
    path('details/', profile_details, name='profile-details'),
    path('create/', create_profile, name='create-profile'),

]