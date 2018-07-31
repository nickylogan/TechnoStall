from django.db import models
from django.utils import timezone

class Item(models.Model):
  item_name = models.CharField(max_length=50)
  item_price = models.FloatField()
  created_date = models.DateTimeField(default=timezone.now)
  description = models.TextField(null=True, blank=True)
  
  def __str__(self):
    return "<Item> %s : Rp %s" % (self.item_name, self.item_price)