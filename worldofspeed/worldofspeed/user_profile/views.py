from worldofspeed.core.utils import get_profile, tot_price
from django.shortcuts import render, redirect

from worldofspeed.user_profile.forms import ProfileDelForm, CreateProfileForm, EditProfileForm
from worldofspeed.user_profile.models import Profile


def create_profile(request):

    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}

    return render(request, 'profile-create.html', context)


def edit_profile(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {'profile': profile,
               "form": form}

    return render(request, 'profile-edit.html',context)




def profile_details(request):
    profile = get_profile()
    cars_count = profile.cars.count()
    price_total = tot_price()

    print(profile.first_name, " ", profile.last_name)

    context = {'profile':profile,
               "cars_count": cars_count,
               "price_total": price_total}

    print(price_total)

    return render(request, 'profile-details.html', context)

def delete_profile(request):
    profile = get_profile()
    form = ProfileDelForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'profile':profile,
        "form":form
    }

    return render(request, 'profile-delete.html', context)




