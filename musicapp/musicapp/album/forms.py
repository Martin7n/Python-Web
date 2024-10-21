from musicapp.album.models import Album
from django import forms


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('__all__')

class CreateAlbumForm(AlbumBaseForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs["placeholder"] = self.fields[fieldname].label


class EditAlbumForm(AlbumBaseForm):
    class Meta:
        model = Album
        exclude = ('owner',)

    #     labels = {
    #     'album_name': "Album:",
    #     'artist': 'Artist:',
    #     'genre': 'Genre:',
    #     'description': 'description:',
    #     "album_picture_url": 'imgUrl',
    #     "price": 'Price:'
    # }
    #
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     # self.fields['album_name'].widget.attrs['labels'] = 'Name:'
    #     # self.fields['artist'].widget.attrs['labels'] = 'Artist:'
    #     # self.fields['genre'].widget.attrs['labels'] = 'Genre:'
    #     # self.fields['description'].widget.attrs['labels'] = 'description'
    #     # self.fields['album_picture_url'].widget.attrs['labels'] = 'imgUrl'
    #     # self.fields['price'].widget.attrs['labels'] = 'Price:'


class AlbumDelForm(forms.ModelForm):
    class Meta:

        model = Album
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (k, field) in self.fields.items():
            # field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
