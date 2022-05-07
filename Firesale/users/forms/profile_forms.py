from django.forms import ModelForm, widgets
from users.models import Profiles
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



# Ætla fá þetta til að virka
class CustomRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


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
        widgets = {
            'image': widgets.FileInput(attrs={'class': 'form-control'})
        }