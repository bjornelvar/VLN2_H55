from django.shortcuts import render, redirect

# Create your views here.
from checkout.forms.forms import ShippingForm, BillingForm


def shipping_info(request):
    if request.method == 'POST':
        shipping_form = ShippingForm(request.POST)
        if shipping_form.is_valid():
            shipping_form.save()
            # return redirect('login')
    else:
        shipping_form = ShippingForm()

    context = {'shipping_form': shipping_form}

    return render(request, 'checkout/checkout.html', context)


def billing_info(request):
    if request.method == 'POST':
        billing_form = BillingForm(request.POST)    # Sækir í users>forms>profile_forms.py
        if billing_form.is_valid():
            billing_form.save()
            # return redirect('login')
    else:
        billing_form = BillingForm()

    context = {'billing_form': billing_form}

    return render(request, 'checkout/checkout.html', context)