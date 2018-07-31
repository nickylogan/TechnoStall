from django.db import models
from django.conf import settings
from django.utils import timezone


class Item(models.Model):
    item_name = models.CharField(max_length=50, unique=True)
    item_price = models.FloatField()
    item_stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s | %d - %s" % (self.item_name, self.item_stock, 'Rp {0:,}'.format(self.item_price))


class Restock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    restock_amount = models.IntegerField()
    restock_cost = models.FloatField()
    PIC = models.CharField(max_length=50)

    def __str__(self):
        return "%d %s(s) by %s for %s" % (self.restock_amount, self.item.item_name,
                                          self.PIC, 'Rp {0:,}'.format(self.restock_cost))


class Sale(models.Model):
    user_on_duty = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price_sold = models.FloatField(default=item.item_price)
