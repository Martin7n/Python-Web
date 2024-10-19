from fruitipedia.fruit.models import Fruit
from django import forms

class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)


class CreateFruitForm(FruitBaseForm):
    class Meta:
        model = Fruit
        exclude = ("owner",)

        labels = {
            'fruit_name': '',
            'fruit_image_url': '',
            'description': '',
            'nutrition_info': '',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)





        self.fields['fruit_name'].widget.attrs['placeholder'] = "Fruit Name"
        self.fields['fruit_image_url'].widget.attrs['placeholder'] = "Fruit Image URL"
        self.fields['description'].widget.attrs['placeholder'] = "Fruit Description"
        self.fields['nutrition'].widget.attrs['placeholder'] = "Nutrition Info"



class EditFruitForm(FruitBaseForm):
    pass

class DeleteFruitForm(FruitBaseForm):
    pass
