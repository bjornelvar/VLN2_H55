from django.forms import ModelForm, widgets
from django import forms
from items.models import Items, ItemImages


class CreateListingForm(ModelForm):
    # image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Items
        CONDITION_CHOICES = [('Like New', 'Like New'), ('Very Good', 'Very Good'),
                             ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')]
        CATEGORY_CHOICES = [('Books', 'Books'), ('Transportation', 'Transportation'),
                            ('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Furniture', 'Furniture'),
                            ('Sports', 'Sports'), ('Home', 'Home'), ('Other', 'Other')]
        exclude = ['id', 'seller', 'sold']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.Select(choices=CONDITION_CHOICES, attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'category': widgets.Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-control'}),
            # 'subcategory': widgets.Select(attrs={'class': 'form-control'}),
            #'image': widgets.FileInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

class CreateListingFormImages(ModelForm):

    class Meta:
        model = ItemImages
        exclude = ['id', 'item']
        labels = {
            'image': "Attach images"
        }
        widgets = {
            'image': widgets.FileInput(attrs={'class': 'form-control', 'multiple': True})
        }