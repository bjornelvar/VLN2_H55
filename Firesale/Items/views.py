from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from items.forms.new_listing_form import CreateListingForm

# Create your views here.
# @login_required(login_url="/%2Fuserslogin")


def index(response):
    return render(response, 'items/index.html')


def create_listing(request):
    if request.method == 'POST':
        print(1)
    else:
        form = CreateListingForm()
    return render(request, 'items/create_listing.html', {
        'form': form
    })
