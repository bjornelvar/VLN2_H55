from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
# @login_required(login_url="/%2Fuserslogin")
def index(response):
    return render(response, 'items/index.html')
