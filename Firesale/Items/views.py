from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from items.forms.new_listing_form import CreateListingForm
from items.models import Items
from items.models import Categories


# Create your views here.
# @login_required(login_url="/%2Fuserslogin")


def index(response):
    context = {'items': Items.objects.all().order_by('name')}
    return render(response,   'items/index.html', context)


def get_category_list(response):
    context = {'categories': Categories.objects.all().order_by('name')}
    return render(response,   'items/category_list.html', context)


# def get_items_in_category(response):
#     context = {'items_category': Items.objects.filter(category=self.category).order_by('name')}
#     return render(response,   'items/index.html', context)


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


def get_item_by_id(request,id):
    return render(request, 'items/item_details.html', {
        'item': get_object_or_404(Items, pk=id)
    })
