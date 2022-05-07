from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.models import Profiles
from users.forms.profile_forms import *
from items.models import Items


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(request, 'users/register.html', {
#         'form': UserCreationForm()
#     })

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegisterForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)

@login_required
def my_listings(response):
    context = {'items': Items.objects.filter(seller_id=response.user.id).order_by('name')}
    return render(response,   'users/my_listings.html', context)


def profile(request):
    profile = Profiles.objects.filter(user=request.user).first()
    if request.method == 'POST':
        btn = request.POST.get('name')
        form = ProfileForm(instance=profile, data=request.POST)

        if 'image' == btn:
            form = UploadImage(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    return render(request, 'users/profile_edit.html', {
        'form': ProfileForm(instance=profile),      # ProfileForm fallið er í users>forms>profile_forms.py
        'form1': UploadImage(instance=profile),     # UploadImage fallið er í users>forms>profile_forms.py
    })

def show_profile(request):
    return render(request, 'users/profile.html')