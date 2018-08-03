from django.db import models
from django.utils import timezone
from .item import Item, Restock

class RestockItemManager(models.Manager):
    pass

class RestockItem(models.Model):
    restock = models.ForeignKey(Restock, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    restock_item_amount = models.PositiveIntegerField()
    restock_item_total_cost = models.FloatField()

    objects = RestockItemManager()

    def __str__(self):
        return "%d %s(s) for %d" % (self.item.item_name, self.restock_item_amount, self.restock_item_total_cost)