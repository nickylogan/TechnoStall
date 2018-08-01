from django.db import models
from django.utils import timezone

class Item(models.Model):
    item_name = models.CharField(max_length=50, unique=True)
    item_price = models.FloatField()
    item_stock = models.PositiveIntegerField(default=0)
    availability = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s | %d - %s" % (self.item_name, self.item_stock, 'Rp {0:,}'.format(self.item_price))