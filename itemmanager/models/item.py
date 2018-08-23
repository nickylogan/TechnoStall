from django.db import models
from django.utils import timezone

class ItemManager(models.Manager):
    pass
    
class Item(models.Model):
    item_name = models.CharField(max_length=50, unique=True)
    item_price = models.FloatField()
    item_availability = models.BooleanField(default=True)
    item_image = models.ImageField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

    objects = ItemManager()

    def __str__(self):
        return "%s | %d - %s" % (self.item_name, self.item_stock, 'Rp {0:,}'.format(self.item_price))

    @property
    def item_stock(self):
        from . import SaleItem, RestockItem
        sales = SaleItem.objects.sale_total_amount(item=self)
        restocks = RestockItem.objects.restock_total_amount(item=self)
        return restocks - sales