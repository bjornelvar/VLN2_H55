from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView

from checkout.models import ShippingInformation



class CheckoutWizard2(SessionWizardView):
    template_name = 'checkout/checkout.html'
    instance = None

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = ShippingInformation()
        return self.instance

    def done(self, form_list, **kwargs):
        self.instance.save()



class CheckoutWizard(SessionWizardView):
    template_name = 'checkout/checkout.html'
    def dispatch(self, request, *args, **kwargs):
        self.instance = ShippingInformation()
        self.instance.user_id = request.user.id
        print(self.instance)
        print('dispatch')
        return super(CheckoutWizard, self).dispatch(request, *args, **kwargs)

    def get_form_instance(self, step):
        print('get')
        return self.instance

    def done(self, form_list, **kwargs):
        print('done')
        self.instance.save()
        return render(self.request, "checkout/done.html")





# class CheckoutWizard(SessionWizardView):
#     template_name = "checkout/checkout.html"

    # def get_form_instance(self, step):
    #     if self.instance is None:
    #         self.instance = ShippingInformation()
    #     return self.instance

    # def done(self, form_list, **kwargs):
    #     form_data = process_form_data(form_list)
    #     print('done fall eftir process')
    #     return render(self.request, "checkout/done.html", {"form_data": form_data})



# def process_form_data(form_list):
#     form_data = [form.cleaned_data for form in form_list]
#     print(f'fyrsta form: {form_data[0]}')
#     print(form_data[0].values())
#     return form_data















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