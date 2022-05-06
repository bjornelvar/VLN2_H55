from django.forms import ModelForm, widgets
from users.models import Profiles
from django.contrib.auth.forms import UserCreationForm
from django import forms



# Ætla fá þetta til að virka
# class CustomRegisterForm(UserCreationForm):
#     class Meta:
#         model = Profiles
#         fields = ['user', 'password1', 'password2']
#         widgets = {
#             'username': widgets.TextInput(attrs={'class': 'form-control'}),
#             'password1': widgets.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': widgets.PasswordInput(attrs={'class': 'form-control'}),
#         }


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