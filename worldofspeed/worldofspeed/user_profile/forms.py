
from django import forms

from worldofspeed.user_profile.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'password', "age", "email")
        widgets = {
            'password': forms.PasswordInput(),
        }



class EditProfileForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ('__all__')
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }



class ProfileDelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (k, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
