from django.db import models
from django.conf import settings
from django.utils import timezone
from .item import Item

class Sale(models.Model):
    user_on_duty = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sale_amount = models.IntegerField()
    sale_price_custom = models.FloatField(blank=True,null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%d %s(s)" % (self.item.item_name, self.sale_amount)