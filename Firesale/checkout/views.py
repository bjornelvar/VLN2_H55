from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from formtools.wizard.views import SessionWizardView

from checkout.forms.forms import OrderForm, ShippingForm, PaymentForm, RateSellerForm
from checkout.models import ShippingInformation
#
from items.models import Items
from bids.models import Bids
from users.models import Ratings, Profiles
from django.db.models import Max
from django.db.models import Avg


FORMS = [("shipping", ShippingForm),
         ("payment", PaymentForm),
         ("rating", RateSellerForm),
         ("confirmation", OrderForm)]

TEMPLATES = {"shipping": "checkout/shipping.html",
             "payment": "checkout/payment.html",
             "rating": "checkout/rating.html",
             "confirmation": "checkout/confirmation.html"}





# def success_view(request):
#     return redirect('my-orders')
#
# def review_view(request):
#     print(f'review {CheckoutWizard.instance_dict}')
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         print(CheckoutWizard.instance)
#         if form.is_valid():
#             form.save()
#             CheckoutWizard.instance.save()
#             return render(request, 'checkout/success.html', {'instance': CheckoutWizard.instance})



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


    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]


    def get_context_data(self, form, **kwargs):
        context = super(CheckoutWizard, self).get_context_data(form, **kwargs)
        item = get_object_or_404(Items, id=self.kwargs['id'])
        max_bid = Bids.objects.filter(item_id=item.id).latest('bidamount')

        # item = get_object_or_404(Items, pk=self.kwargs['id'])
        context.update({'item': item})
        context.update({'max_bid': max_bid.bidamount})
        context.update({'shipping_info': CheckoutWizard.get_cleaned_data_for_step(self, 'shipping')})
        context.update({'payment_info': CheckoutWizard.get_cleaned_data_for_step(self, 'payment')})
        context.update({'rating_info': CheckoutWizard.get_cleaned_data_for_step(self, 'rating')})
        # print(context)
        # print(context["rating_info"]["rating"])
        return context

    def done(self, form_list, **kwargs):
        item = get_object_or_404(Items, pk=self.kwargs['id'])
        item.sold = True
        item.save()
        rating = CheckoutWizard.get_cleaned_data_for_step(self, 'rating')
        if rating is not None:
            rating_final = rating["rating"]
            review = Ratings.objects.create(rating=rating_final, rated_user_id = item.seller_id, rated_by_id = self.request.user.id)
            review.save()
            ratings_for_seller = Ratings.objects.filter(rated_user_id=item.seller_id).aggregate(Avg('rating'))
            avg_rating = ratings_for_seller['rating__avg']
            seller = get_object_or_404(Profiles, pk=item.seller_id)
            seller.rating = avg_rating
            seller.save()
        return redirect('my-orders')












# class CheckoutWizard(SessionWizardView):
#     template_name = 'checkout/checkout.html'
#
#
#     def dispatch(self, request, id, *args, **kwargs):
#         print(f"REQUEST: {request}")
#         print(f"ID: {id}")
#         self.instance = ShippingInformation()
#         self.sold = Items()
#         self.instance.user_id = request.user.id
#         print('dispatch')
#         # print(**kwargs)
#         return super(CheckoutWizard, self).dispatch(request, id, *args, **kwargs)
#
#     def get_form_instance(self, step):
#         print('get')
#         return self.instance
#
#     def done(self, form_list, **kwargs):
#         WizardView.get_all_cleared_data(self)
#         print('done')
#         self.instance.save()
#         print('form is saved', self.instance.first_name)
#         self.sold.save()
#         print('sold form is saved', self.sold)
#
#         return redirect('my-orders')
















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