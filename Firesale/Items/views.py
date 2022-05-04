from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from items.models import Items


# Create your views here.
# @login_required(login_url="/%2Fuserslogin")
def index(response):
    context = {'items': Items.objects.all().order_by('name')}
    return render(response, 'items/index.html')