from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ('item_name', 'item_price', 'item_image', 'description')

class SaleForm(forms.Form):
  pass

class RestockForm(forms.Form):
  pass