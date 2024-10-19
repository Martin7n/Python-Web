from django.shortcuts import render, redirect

from fruitipedia.fruit.models import Fruit
from fruitipedia.user_profile.forms import EditProfileForm, DeleteProfileForm, CreateProfileForm
from fruitipedia.user_profile.models import Profile


# Create your views here.


def create_profile(request):

    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        "form": form,

    }

    return render(request, 'create-profile.html', context)

def profile_details(request):

    profile = Profile.objects.first()
    prof_posts = Fruit.objects.select_related('owner').count()
    context = {
        "profile": profile,
        "prof_posts": prof_posts
    }

    return render(request, 'details-profile.html', context)

def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {
        "profile": profile,
        "form": form,
    }
    return render(request,"edit-profile.html", context)

def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    form = DeleteProfileForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('dashboard')

    context = {
        "profile": profile,
    }
    return render(request, 'delete-profile.html', context)

