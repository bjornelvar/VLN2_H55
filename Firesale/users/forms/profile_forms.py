from django.forms import ModelForm, widgets
from users.models import Profiles
from items.models import Items, ItemImages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


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
        exclude = ['id', 'rating', 'image', 'user', 'get_notifications']
        widgets = {
            'bio': widgets.Textarea(attrs={'class': 'form-control'})
        }


class UploadImageForm(ModelForm):
    class Meta:
        model = Profiles
        exclude = ['id', 'rating', 'user', 'bio', 'get_notifications']
        labels = {'image': 'Change profile picture:'}
        widgets = {
            'image': widgets.FileInput(attrs={'class': 'form-control'})
        }

class EditListingForm(ModelForm):
    class Meta:
        model = Items
        CONDITION_CHOICES = [('Like New', 'Like New'), ('Very Good', 'Very Good'),
                             ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')]
        exclude = ['id', 'listdate', 'seller', 'has_accepted_bid', 'sold']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.Select(choices=CONDITION_CHOICES, attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

class AddListingPicturesForm(ModelForm):
    class Meta:
        model = ItemImages
        fields = ['image']
        labels = {
            'image': 'Attatch images'
        }
        widgets = {
            'image': widgets.FileInput(attrs={'class': 'form-control', 'multiple': True})
        }