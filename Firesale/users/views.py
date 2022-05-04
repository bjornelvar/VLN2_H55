from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.models import Profiles
# Create your views here.

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
        print(1)
    return render(request, 'users/profile.html', {
        'form': ''
    })