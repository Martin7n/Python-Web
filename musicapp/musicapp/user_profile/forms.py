
from django import forms

from musicapp.user_profile.models import Profile



class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')



class ProfileDelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (k, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
