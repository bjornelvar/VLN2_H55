from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from users.models import Profiles
from django.contrib import messages
from users.forms.profile_forms import *
from items.models import Items
from bids.models import Bids
from django.db.models import Max
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User




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
    context = {'items': Items.objects.filter(seller_id=response.user.id).order_by('listdate').annotate(max_offer = Max('bids__bidamount'))} # Reverse order líka?
    return render(response,   'users/my_listings.html', context)

@login_required
def my_bids(response):
    context = {'bids': Bids.objects.filter(bidder_id=response.user.id).order_by('biddate'),
               'max_bids': Items.objects.all().annotate(max_offer = Max('bids__bidamount'))} # Reverse order líka?
    return render(response,   'users/my_bids.html', context)

@login_required
def profile(request):
    profile = Profiles.objects.filter(user=request.user).first()
    user = User.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        btn = request.POST.get('name')
        form1 = ProfileForm(instance=profile, data=request.POST)
        form2 = EditUserForm(instance=user, data=request.POST)

        if 'image' == btn:
            if request.FILES:
                form = UploadImage(request.POST, request.FILES, instance=profile)
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
        'imageform': UploadImage(instance=profile),     # UploadImage fallið er í users>forms>profile_forms.py
        'edituserform': EditUserForm(instance=user),
    })

def accept_bid(request):
    bid = get_object_or_404(Bids, pk=request.GET.get('bid_id'))
    bid.is_accepted = True
    bid.save()
    item = get_object_or_404(Items, pk=bid.item_id)
    item.has_accepted_bid = True
    item.save()
    send_email_notification(bid)

    return redirect('my-listings')

def show_profile(request):
    return render(request, 'users/profile.html')

def send_email_notification(bid):
    # Works badly on @ru.is mails. Probably due to some type of filtering on RU's mail server
    all_bids_on_item = Bids.objects.filter(item_id=bid.item_id)
    print("bid_id: ", bid.id)
    print("bidder_id: ", bid.bidder_id)
    rejected_item_name = Items.objects.filter(id=bid.item_id).first().name
    for user in User.objects.all():
        if user.id == bid.bidder_id:
            winner_email = user.email
            print("winner_email:", winner_email)
            send_mail("FireSale: Bid accepted!", f"Congratulations! Your bid of ${bid.bidamount} for {rejected_item_name} has been accepted! Go to the MY BIDS section on your FireSale dashboard to complete your order!", settings.EMAIL_HOST_USER, [winner_email], fail_silently=False)
            print(" Winner Email should be sent")

    for rejected_bid in all_bids_on_item:
        if rejected_bid.bidder_id != bid.bidder_id:
            rejected_email = User.objects.filter(id=rejected_bid.bidder_id).first().email
            print("rejected email:", rejected_email)
            send_mail("FireSale: Bid rejected!", f"Your bid of ${rejected_bid.bidamount} for {rejected_item_name} has been rejected! Go to the MY BIDS section on your FireSale dashboard to see the other bids.", settings.EMAIL_HOST_USER, [rejected_email], fail_silently=False)
            print(" Rejected Email should be sent")