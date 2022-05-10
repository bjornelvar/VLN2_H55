from django.shortcuts import render, redirect

# Create your views here.
from checkout.forms.forms import ShippingForm, BillingForm, PaymentForm


def checkout_info(request):
    if request.method == 'POST':
        shipping_form = ShippingForm(request.POST)
        billing_form = BillingForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if shipping_form.is_valid() and billing_form.is_valid() and payment_form.is_valid():
            shipping_form.save() # þurfum í raun bara að geyma þetta
            # billing_form.save()
            # payment_form.save()
            # return redirect('login')
    else:
        shipping_form = ShippingForm()
        billing_form = BillingForm()
        payment_form = PaymentForm()

    context = {'shipping_form': shipping_form,
               'billing_form': billing_form,
               'payment_form': payment_form}

    return render(request, 'checkout/checkout.html', context)