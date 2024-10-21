from musicapp.album.models import Album
from musicapp.user_profile.models import Profile


def get_profile():
    profile = Profile.objects.first()
    return profile

def get_all_albums():
    albums = Album.objects.all()
    return albums
