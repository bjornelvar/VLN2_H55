from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from users.models import Profiles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from users.forms.profile_forms import *
from items.models import Items
from bids.models import Bids
from django.db.models import Max
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from checkout.models import Orders
from django.contrib.auth import authenticate, login





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
            new_user = form.save()
            # messages.success(request, 'Your account has been created! You will now be logged in.')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('home:home-index')
    else:
        form = CustomRegisterForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)

@login_required
def my_listings(request):
    sold_filter = None
    if "sold" in request.GET:
        sold = request.GET["sold"]
        if sold == "false":
            items = Items.objects.filter(seller_id=request.user.id).order_by('has_accepted_bid', '-listdate') \
                .annotate(max_offer=Max('bids__bidamount')).filter(sold=False)
            sold_filter = False
        else:
            items = Items.objects.filter(seller_id=request.user.id).order_by('has_accepted_bid', '-listdate') \
                .annotate(max_offer=Max('bids__bidamount'))
            sold_filter = True
    else:
        items = Items.objects.filter(seller_id=request.user.id).order_by('has_accepted_bid', '-listdate') \
            .annotate(max_offer=Max('bids__bidamount'))

    paginator = Paginator(items,5)
    page_num = request.GET.get('page', 1)
    try:
        page = paginator.get_page(page_num)
    except EmptyPage or PageNotAnInteger:
        page = paginator.page(1)
    context = {'bids':Bids.objects.all(), 'items': page, 'sold_filter': sold_filter} # Reverse order líka?
    return render(request,   'users/my_listings.html', context)

@login_required
def my_orders(request):

    orders = Orders.objects.filter(receiver_id=request.user.id)
    paginator = Paginator(orders,5)
    page_num = request.GET.get('page', 1)
    try:
        page = paginator.get_page(page_num)
    except EmptyPage or PageNotAnInteger:
        page = paginator.page(1)

    context = {'orders': page}
    return render(request,   'users/my_orders.html', context)

@login_required
def my_bids(request):
    bids = Bids.objects.filter(bidder_id=request.user.id).order_by('biddate')
    bids1 = bids.filter(item__has_accepted_bid=False)
    bids2 = bids.filter(is_accepted=True)
    bids = bids1 | bids2
    bids = bids.filter(item__sold=False)
    paginator = Paginator(bids,5)
    page_num = request.GET.get('page', 1)
    try:
        page = paginator.get_page(page_num)
    except EmptyPage or PageNotAnInteger:
        page = paginator.page(1)

    # user_bids = Bids.objects.filter(bidder_id=request.user.id).order_by('biddate')
    context = {'bids': page, 'max_bids': Items.objects.all().annotate(max_offer = Max('bids__bidamount'))} # Reverse order líka?
    return render(request,   'users/my_bids.html', context)

@login_required
def edit_profile(request):
    profile = Profiles.objects.filter(user=request.user).first()
    user = User.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        btn = request.POST.get('name')
        form1 = ProfileForm(instance=profile, data=request.POST)
        form2 = EditUserForm(instance=user, data=request.POST)

        if 'image' == btn:
            if request.FILES:
                form = UploadImageForm(request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    image = form.save(commit=False)
                    image.user = request.user
                    image.save()
                    return redirect('profile')
            else:
                messages.error(request, 'No image attached')

        else:
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
        'imageform': UploadImageForm(instance=profile),     # UploadImage fallið er í users>forms>profile_forms.py
        'edituserform': EditUserForm(instance=user),
    })

def accept_bid(request):
    bid = get_object_or_404(Bids, pk=request.GET.get('bid_id'))
    print(bid)
    bid.is_accepted = True
    bid.save()
    item = get_object_or_404(Items, pk=bid.item_id)
    item.has_accepted_bid = True
    item.save()
    send_email_notification(bid)

    return redirect('my-listings')

def show_profile(request, id=None):
    if id:
        return render(request, 'users/user_profile.html', {
            'some_user': get_object_or_404(User, pk=id)
        })
    return render(request, 'users/profile.html')

def send_email_notification(bid):
    # Works badly on @ru.is mails. Probably due to some type of filtering on RU's mail server
    all_bids_on_item = Bids.objects.filter(item_id=bid.item_id)
    print("bid_id: ", bid.id)
    print("bidder_id: ", bid.bidder_id)
    rejected_item_name = Items.objects.filter(id=bid.item_id).first().name
    for user in User.objects.all():
        if user.id == bid.bidder_id:
            if user.profiles.get_notifications:
                winner_email = user.email
                print("winner_email:", winner_email)
                send_mail("FireSale: Bid accepted!", f"Congratulations! Your bid of ${bid.bidamount} for {rejected_item_name} has been accepted! Go to the MY BIDS section on your FireSale dashboard to complete your order!", settings.EMAIL_HOST_USER, [winner_email], fail_silently=False)
                print(" Winner Email should be sent")

    for rejected_bid in all_bids_on_item:
        if rejected_bid.bidder_id != bid.bidder_id:
            rejected_user = User.objects.filter(id=rejected_bid.bidder_id).first()
            if rejected_user.profiles.get_notifications:
                rejected_email = rejected_user.email
                print("rejected email:", rejected_email)
                send_mail("FireSale: Bid rejected!", f"Your bid of ${rejected_bid.bidamount} for {rejected_item_name} has been rejected! Go to the MY BIDS section on your FireSale dashboard to see the other bids.", settings.EMAIL_HOST_USER, [rejected_email], fail_silently=False)
                print(" Rejected Email should be sent")


def edit_listing(request, id):
    item = get_object_or_404(Items, pk=id)

    if request.method == 'POST':
        form = EditListingForm(instance=item, data=request.POST)
        if form.is_valid():
            item_edits = form.save(commit=False)
            item_edits.seller_id = request.user.id
            item.save()
            if request.FILES:
                form_images = AddListingPicturesForm(request.POST, request.FILES)
                if form_images.is_valid():
                    for image in request.FILES.getlist('image'):
                        ItemImages.objects.create(image=image, item_id=item.id)

            return redirect('my-listings')

    return render(request, 'users/edit_listing.html', {
        'form': EditListingForm(instance=item),
        'imageform': AddListingPicturesForm(),
        'item': item
    })

def delete_item(request,id):
    item = get_object_or_404(Items, pk=id)
    item.delete()
    return redirect('my-listings')

def user_settings(request):
    return render(request, 'users/user_settings.html')

def toggle_notifications(request):
    profile = Profiles.objects.get(pk=request.POST['id'])
    profile.get_notifications = request.POST['get_notifications'] == 'true'
    profile.save()
    return HttpResponse(status=200)

def send_email_verify_email(request):
    pass