from django.urls import path, include

from musicapp.album.views import album_details, delete_album, create_album, edit_album

urlpatterns = [
    path('add/', create_album, name='add-album'),
    path("<int:pk>/",
         include(
        [path('details/',album_details, name="album_details"),
         path('edit/', edit_album, name="edit_album"),
         path('delete/', delete_album, name="delete_album"),

         ])
         )
]


