from django.shortcuts import render, redirect

from musicapp.album.forms import CreateAlbumForm, EditAlbumForm, AlbumDelForm
from musicapp.album.models import Album
from musicapp.core.utils import get_profile, get_all_albums


# Create your views here.


def index(request):
    profile = get_profile()
    albums = get_all_albums()

    context ={
        "profile":profile,
        "albums":albums
    }
    return render(request,"home-no-profile.html", context)

def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
         "album": album}

    return render(request,"album-details.html", context)


def create_album(request):
    form = CreateAlbumForm()

    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form": form}
    return render(request, 'album-add.html', context)

def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = EditAlbumForm(instance=album)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        print(form)
        if form.is_valid():
            # form.instance.owner_id = get_profile().pk
            form.save()
            return redirect('home')

    context = {
        "album": album,
        "form": form}

    return render(request,"album-edit.html", context)

def delete_album(request, pk):
    album = Album.objects.get(pk=pk)

    form = AlbumDelForm(instance=album)
    if request.method == "POST":
        album.delete()
        return redirect('home')

    context = {
        "album": album,
        "form":form
    }

    return render(request,"album-delete.html", context)


