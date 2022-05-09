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


class EditUserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['user_permissions', 'groups', 'password', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'first_name', 'last_name', 'email']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        exclude = ['id', 'rating', 'image', 'user']
        widgets = {
            'bio': widgets.Textarea(attrs={'class': 'form-control'})
        }


class UploadImage(ModelForm):
    class Meta:
        model = Profiles
        exclude = ['id', 'rating', 'user', 'bio']
        widgets = {
            'image': widgets.FileInput(attrs={'class': 'form-control'})
        }