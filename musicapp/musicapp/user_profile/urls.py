from django.shortcuts import render
from django.urls import path, include

from musicapp.user_profile.views import create_profile, delete_profile, profile_details

# Create your views here.



urlpatterns = [
    path('delete/', delete_profile, name='delete-profile'),
    path('details/', profile_details, name='profile-details'),
    path('create/', create_profile, name='create-profile'),

]