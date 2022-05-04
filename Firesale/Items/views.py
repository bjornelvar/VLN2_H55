from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from items.forms.new_listing_form import CreateListingForm
from items.models import Items


# Create your views here.
# @login_required(login_url="/%2Fuserslogin")


def index(response):
    context = {'items': Items.objects.all().order_by('name')}
    return render(response,   'items/index.html', context)


def create_listing(request):
    if request.method == 'POST':
        form = CreateListingForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller_id = request.user.id
            item.save()
            return redirect('items-index')

    else:
        form = CreateListingForm()
    return render(request, 'items/create_listing.html', {
        'form': form
    })


def get_user_id(request):
    return request.user.id
