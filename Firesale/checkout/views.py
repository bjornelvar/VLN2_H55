from django.shortcuts import redirect, get_object_or_404
from formtools.wizard.views import SessionWizardView
from checkout.forms.forms import OrderForm, ShippingForm, PaymentForm, RateSellerForm
from items.models import Items
from bids.models import Bids
from users.models import Ratings, Profiles
from checkout.models import Orders
from django.db.models import Avg


FORMS = [("shipping", ShippingForm),
         ("payment", PaymentForm),
         ("rating", RateSellerForm),
         ("confirmation", OrderForm)]

TEMPLATES = {"shipping": "checkout/shipping.html",
             "payment": "checkout/payment.html",
             "rating": "checkout/rating.html",
             "confirmation": "checkout/confirmation.html"}


class CheckoutWizard(SessionWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super(CheckoutWizard, self).get_context_data(form, **kwargs)
        item = get_object_or_404(Items, id=self.kwargs['id'])
        max_bid = Bids.objects.filter(item_id=item.id).latest('bidamount')
        context.update({'item': item})
        context.update({'max_bid': max_bid.bidamount})
        context.update({'shipping_info': CheckoutWizard.get_cleaned_data_for_step(self, 'shipping')})
        context.update({'payment_info': CheckoutWizard.get_cleaned_data_for_step(self, 'payment')})
        context.update({'rating_info': CheckoutWizard.get_cleaned_data_for_step(self, 'rating')})
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
            order = Orders.objects.create(receiver_id=self.request.user.id, sender_id=item.seller_id, item_id=item.id)
            order.save()
        return redirect('my-orders')
