from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Restock, Sale


@receiver(post_save, sender=Restock)
def save_restock(sender, instance, **kwargs):
    item = instance.item
    item.item_stock += instance.restock_amount
    item.save()


@receiver(post_save, sender=Sale)
def save_sale(sender, instance, **kwards):
    item = instance.item
    item.item_stock -= instance.sale_amount
    item.save()
