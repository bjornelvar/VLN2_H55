from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from items.forms.new_listing_form import CreateListingForm
from items.models import Items
from items.models import Categories
from users.models import Profiles


# Create your views here.
# @login_required(login_url="/%2Fuserslogin")


def index(response):
    context = {'items': Items.objects.all().order_by('name'), 'categories': Categories.objects.all().order_by('name')}
    return render(response,   'items/index.html', context)


def search_items(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        return render(request, 'items/search_items.html', {'search_term': search_term, 'items': Items.objects.filter(name__icontains=search_term),
                                                           'categories': Categories.objects.all().order_by('name')})
    else:
        return render(request, 'items/search_items.html', {})


def get_items_by_category(response, id):
    context = {'items': Items.objects.filter(category_id=id).order_by('name'), 'categories': Categories.objects.all().order_by('name'), 'current_category': id }
    return render(response,   'items/index.html', context)


def create_listing(request):
    if request.method == 'POST':
        form = CreateListingForm(request.POST, request.FILES)
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
    context = {'item': get_object_or_404(Items, pk=id), 'categories': Categories.objects.all().order_by('name'),
               'items': Items.objects.all().order_by('name')}
    return render(request, 'items/item_details.html', context)
