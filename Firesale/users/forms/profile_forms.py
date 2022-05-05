from django.forms import ModelForm, widgets
from users.models import Profiles


class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        exclude = ['id', 'rating', 'user', 'image']
        widgets = {
            'bio': widgets.Textarea(attrs={'class': 'form-control'}),
        }


class UploadImage(ModelForm):
    class Meta:
        model = Profiles
        exclude = ['id', 'rating', 'user', 'bio']