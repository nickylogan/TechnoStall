from django.db import models
from django.utils import timezone
from .item import Item


class Restock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    restock_amount = models.IntegerField()
    restock_cost = models.FloatField()
    restock_PIC = models.CharField(max_length=50)

    def __str__(self):
        return "%d %s(s) by %s for %s" % (self.restock_amount, self.item.item_name,
                                          self.PIC, 'Rp {0:,}'.format(self.restock_cost))