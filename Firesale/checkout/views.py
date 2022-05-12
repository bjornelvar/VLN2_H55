from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView


class CheckoutWizard(SessionWizardView):
    template_name = "checkout/checkout.html"

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return render(self.request, "checkout/done.html", {"form_data": form_data})


def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    return form_data















# def shipping_info(request):
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
# def payment_info(request):
#     if request.method == 'POST':
#         payment_form = PaymentForm(request.POST)
#         if payment_form.is_valid():
#             # payment_form.save()
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