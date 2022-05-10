from django.forms import ModelForm, widgets
from bids.models import Bids


class CreateBidsForm(ModelForm):

    class Meta:
        model = Bids
        exclude = ['id', 'bidder', 'item', 'biddate', 'is_accepted']


# class AcceptBidsForm(ModelForm):
#
#     class Meta:
#         model = Bids
#         exclude = ['id', 'bidder', 'item', 'biddate', 'bidamount']
#         widgets = {
#             'is_accepted': widgets.CheckboxInput()
#         }