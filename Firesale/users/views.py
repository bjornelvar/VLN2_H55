from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.models import Profiles
from users.forms.profile_forms import *


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {
        'form': UserCreationForm()
    })


def profile(request):
    profile = Profiles.objects.filter(user=request.user).first()
    if request.method == 'POST':
        btn = request.POST.get('name')
        form = ProfileForm(instance=profile, data=request.POST)

        if 'image' == btn:
            form = UploadImage(instance=profile, data=request.FILES)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

    return render(request, 'users/profile.html', {
        'form': ProfileForm(instance=profile),      # ProfileForm fallið er í users>forms>profile_forms.py
        'form1': UploadImage(instance=profile),     # UploadImage fallið er í users>forms>profile_forms.py
    })