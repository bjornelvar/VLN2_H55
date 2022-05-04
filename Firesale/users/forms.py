from django import forms
from .models import *

class ProfileImgForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_Picture']