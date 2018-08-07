from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from . import Item, Restock

class RestockItemManager(models.Manager):
    def filter_restock(self, restock):
        return super().get_queryset().filter(restock=restock)
    
    def filter_item(self, item):
        return super().get_queryset().filter(item=item)

class RestockItem(models.Model):
    restock = models.ForeignKey(Restock, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    restock_item_amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    restock_item_total_cost = models.FloatField()

    objects = RestockItemManager()

    class Meta:
        unique_together = (("restock", "item"))

    def __str__(self):
        return "%d %s(s) for %d" % (self.item.item_name, self.restock_item_amount, self.restock_item_total_cost)