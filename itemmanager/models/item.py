from django.db import models
from django.utils import timezone

class ItemManager(models.Manager):
    pass
    
class Item(models.Model):
    item_name = models.CharField(max_length=50, unique=True)
    item_price = models.FloatField()
    item_stock = models.PositiveIntegerField(default=0)
    item_availability = models.BooleanField(default=True)
    item_image = models.ImageField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

    objects = ItemManager()

    def __str__(self):
        return "%s | %d - %s" % (self.item_name, self.item_stock, 'Rp {0:,}'.format(self.item_price))