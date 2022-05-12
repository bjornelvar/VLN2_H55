from django.shortcuts import render, redirect
from django.template.context_processors import request
from formtools.wizard.views import SessionWizardView

from checkout.forms.forms import ReviewForm, ShippingForm, PaymentForm
from checkout.models import ShippingInformation
#
def success_view(request):
    return render(request, 'checkout/success.html', {'instance': CheckoutWizard.instance_dict})

def review_view(request):
    print(f'review {CheckoutWizard.instance_dict}')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        print(CheckoutWizard.instance)
        if form.is_valid():
            form.save()
            CheckoutWizard.instance.save()
            return render(request, 'checkout/success.html', {'instance': CheckoutWizard.instance})



# class CheckoutWizard2(SessionWizardView):
#     template_name = 'checkout/checkout.html'
#     instance = None
#
#     def get_form_instance(self, step):
#         if self.instance is None:
#             self.instance = ShippingInformation()
#         return self.instance
#
#     def done(self, form_list, **kwargs):
#         self.instance.save()


class CheckoutWizard(SessionWizardView):
    template_name = 'checkout/checkout.html'

    def dispatch(self, request, id, *args, **kwargs):
        self.instance = ShippingInformation()
        self.instance.user_id = request.user.id
        print('dispatch')
        # print(**kwargs)
        return super(CheckoutWizard, self).dispatch(request, id, *args, **kwargs)

    def get_form_instance(self, step):
        print('get')
        return self.instance

    def done(self, form_list, **kwargs):
        print('done')
        self.instance.save()
        print('form is saved', self.instance.first_name)
        return render(self.request, "checkout/success.html", {'instance': self.instance})
















# def shipping_view(request):
#     if request.method == 'POST':
#         shipping_form = ShippingForm(request.POST)
#         if shipping_form.is_valid():
#             # shipping_form.save()
#             return redirect('payment')
#     else:
#         shipping_form = ShippingForm()
#
#     context = {'shipping_form': shipping_form}
#     return render(request, 'checkout/shipping.html', context)
#
#
# def payment_view(request):
#     if request.method == 'POST':
#         payment_form = PaymentForm(request.POST)
#         if payment_form.is_valid():
#             payment_form.save()
#             return redirect('review')
#     else:
#         payment_form = PaymentForm()
#
#     context = {'payment_form': payment_form}
#     return render(request, 'checkout/payment.html', context)
#
# def item_review(request):
#     return render(request, 'checkout/item_review.html')
#
# def review_info(request):
#     return render(request, 'checkout/review.html')