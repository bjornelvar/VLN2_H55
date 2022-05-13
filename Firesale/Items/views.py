from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from items.forms.new_listing_form import CreateListingForm, CreateListingFormImages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from bids.forms.bids_forms import CreateBidsForm
from bids.models import Bids
from items.models import Items, ItemImages
from items.models import Categories
from django.db.models import Max
import Levenshtein
from django.http import HttpResponse



# @login_required(login_url="/%2Fuserslogin")


def index(request):
    items = Items.objects.filter(has_accepted_bid=False, sold=False).order_by('name')

    if "order_by" in request.GET:
        order_by_val = request.GET["order_by"]
        items = items.order_by(order_by_val)
    else:
        order_by_val = ''

    items = items.annotate(max_offer = Max('bids__bidamount'))
    paginator = Paginator(items,9)
    page_num = request.GET.get('page', 1)
    try:
        page = paginator.get_page(page_num)
    except EmptyPage or PageNotAnInteger:
        page = paginator.page(1)
    context = {'location': "index", 'order_by_val': order_by_val, 'items': page, 'categories': Categories.objects.all().order_by('name') }
    return render(request,   'items/index.html', context)


def search_items(request):
    if "search_val" in request.GET:
        search_val = request.GET["search_val"]
        search_term = search_val.replace("+", " ")
        items = Items.objects.filter(name__icontains=search_term, has_accepted_bid=False , sold=False)
        current_category_name = ''
        category_id = ''

    if "category" in request.GET:
        category_id = request.GET["category"]
        items = items.filter(category_id=category_id)
        current_category_name = Categories.objects.get(id=category_id).name

    if "order_by" in request.GET:
        order_by_val = request.GET["order_by"]
        items = items.order_by(order_by_val)


    items = items.annotate(max_offer=Max('bids__bidamount'))
    paginator = Paginator(items, 1)
    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)
    context = {'location': "search", 'search_val': search_val, 'search_term': search_term, 'items': page,
               'categories': Categories.objects.all().order_by('name'), 'current_category':category_id, 'current_category_name': current_category_name}
    return render(request, 'items/search_items.html', context)



def get_items_by_category(request, id):
    items = Items.objects.filter(category_id=id, has_accepted_bid=False, sold=False).order_by('name').annotate(max_offer = Max('bids__bidamount'))

    if "order_by" in request.GET:
        order_by_val = request.GET["order_by"]
        items = items.order_by(order_by_val)

    items = items.annotate(max_offer=Max('bids__bidamount'))
    paginator = Paginator(items,9)
    page_num = request.GET.get('page', 1)
    try:
        page = paginator.get_page(page_num)
    except EmptyPage or PageNotAnInteger:
        page = paginator.page(1)
    context = {'location': "category", 'items': page, 'categories': Categories.objects.all().order_by('name'), 'current_category': id }
    return render(request,   'items/index-by-category.html', context)

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListingForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller_id = request.user.id
            if request.FILES:
                form_images = CreateListingFormImages(request.POST, request.FILES)
                if form_images.is_valid():
                    item.save()
                    for image in request.FILES.getlist('image'):
                        ItemImages.objects.create(image=image, item_id=item.id)
            else:
                item.save()
                ItemImages.objects.create(item_id=item.id)

            return redirect('my-listings')

    else:
        form = CreateListingForm()
        form_images = CreateListingFormImages()
    return render(request, 'items/create_listing.html', {
        'form': form,
        'form_images': form_images
    })


def get_item_by_id(request, id):
    item = get_object_or_404(Items, pk=id)
    all_items = Items.objects.filter(has_accepted_bid=False)
    all_bids = Bids.objects.all()
    similar_items = get_similar_items(item, all_items)
    try:
        max_bid = Bids.objects.filter(item_id=item.id).latest('bidamount')
    except ObjectDoesNotExist:
        max_bid = None
    context = {'item': item, 'categories': Categories.objects.all().order_by('name'),
               'items': similar_items, 'form': CreateBidsForm(), 'max_bid': max_bid, }

    if request.method == 'POST':
        try:
            bid = all_bids.get(item_id=id, bidder_id=request.user.id)
            form = CreateBidsForm(request.POST, instance=bid)   # If exists adds an instance to the form
        except ObjectDoesNotExist:
            form = CreateBidsForm(request.POST)
        if form.is_valid() and float(request.POST.get('bidamount')) >= item.price and item.seller_id != request.user.id:    # Float? Comparea max bid líka.
            if max_bid is None:
                new_bid = form.save(commit=False)
                new_bid.bidder_id = request.user.id
                new_bid.item_id = id
                messages.success(request, "Bid placed successfully")
                new_bid.save()
            elif float(request.POST.get('bidamount')) > max_bid.bidamount:
                new_bid = form.save(commit=False)
                new_bid.bidder_id = request.user.id
                new_bid.item_id = id
                messages.success(request, "Bid placed successfully")
                new_bid.save()
            else:
                messages.error(request, "Bid must be higher than current bid")

        else:
            messages.error(request, "Bid must be higher than the start price")
    return render(request, 'items/item_details.html', context)


def get_similar_items(main_item, all_items):
    items = []
    for item in all_items:
        if len(items) == 3:
            return items
        if get_string_distance(main_item.name, item.name) < 8 and item.id != main_item.id and item not in items:
            if item.category_id == main_item.category_id:
                items.insert(0, item)
            else:
                items.append(item)
    for item in all_items:
        if len(items) == 3:
            return items
        if item.category_id == main_item.category_id and item.id != main_item.id and item not in items:
            items.append(item)
    return items


def get_string_distance(string1, string2):
    string1_clean = string1.replace(" ", "").replace("-", "")
    string2_clean = string2.replace(" ", "").replace("-", "")
    string1_lower = string1_clean.lower()
    string2_lower = string2_clean.lower()
    # noinspection PyUnresolvedReferences
    return Levenshtein.distance(string1_lower, string2_lower)



