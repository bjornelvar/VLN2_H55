from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.models import Profiles
from users.forms.profile_forms import *
from items.models import Items
from bids.models import Bids


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
        form = CustomRegisterForm(request.POST) # Sækir í users>forms>profile_forms.py
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegisterForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)

@login_required
def my_listings(response):
    context = {'items': Items.objects.filter(seller_id=response.user.id).order_by('listdate')} # Reverse order líka?
    return render(response,   'users/my_listings.html', context)

@login_required
def my_bids(response):
    context = {'items': Items.objects.filter(bids__bidder=response.user.id).order_by('bids__biddate')} # Reverse order líka?
    return render(response,   'users/my_bids.html', context)


def profile(request):
    profile = Profiles.objects.filter(user=request.user).first()
    user = User.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        btn = request.POST.get('name')
        form1 = ProfileForm(instance=profile, data=request.POST)
        form2 = EditUserForm(instance=user, data=request.POST)

        if 'image' == btn:
            form = UploadImage(request.POST, request.FILES, instance=profile)

        if form1.is_valid():
            profile = form1.save(commit=False)
            profile.user = request.user
            profile.save()

        if form2.is_valid():
            user = form2.save(commit=False)
            user.save()
            return redirect('profile')

    return render(request, 'users/profile_edit.html', {
        'bioform': ProfileForm(instance=profile),      # ProfileForm fallið er í users>forms>profile_forms.py
        'imageform': UploadImage(instance=profile),     # UploadImage fallið er í users>forms>profile_forms.py
        'edituserform': EditUserForm(instance=user),
    })

def show_profile(request):
    return render(request, 'users/profile.html')