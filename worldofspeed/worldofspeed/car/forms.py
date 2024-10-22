from worldofspeed.car.models import Car
from django import forms


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('__all__')

class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["car_picture"].widget.attrs["placeholder"] = "https://..."
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for fieldname in self.fields:
    #         self.fields[fieldname].widget.attrs["placeholder"] = self.fields[fieldname].label


class EditCarForm(CarBaseForm):
    class Meta:
        model = Car
        exclude = ('owner',)



    #     labels = {
    #     'album_name': "Car:",
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


class CarDelForm(forms.ModelForm):
    class Meta:

        model = Car
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (k, field) in self.fields.items():
            # field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
