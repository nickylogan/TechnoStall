from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from .item import Item, Sale

class SaleItemManager(models.Manager):
    pass

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sale_amount = models.PositiveIntegerField()
    sale_price = models.FloatField(blank=True,null=True)

    def __str__(self):
        return "%d %s(s) for %d" % (self.item.item_name, self.sale_amount, self.sale_price)
    
    def clean(self):
        errors = {}
        if self.item.item_availability == False:
            errors['item'] = ValidationError(_('Item not available!'), code='invalid')
        if self.sale_amount > self.item.item_stock:
            errors['sale_amount'] = ValidationError(_('Sale amount is larger than stock!'), code='invalid')
        
        if errors:
            raise ValidationError(errors)
    