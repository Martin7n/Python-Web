from musicapp.album.forms import CreateAlbumForm
from musicapp.core.utils import get_profile
from django.shortcuts import render, redirect

from musicapp.user_profile.forms import ProfileDelForm, CreateProfileForm
from musicapp.user_profile.models import Profile


def create_profile(request):

    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'create_profile.html', context)


def profile_details(request):
    profile = get_profile()
    albums = profile.albums.count()

    context = {'profile':profile,
               "albums": albums}



    return render(request, 'profile-details.html', context)

def delete_profile(request):
    profile = get_profile()
    form = ProfileDelForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {
        'profile':profile,
        "form":form
    }

    return render(request, 'profile-delete.html', context)




