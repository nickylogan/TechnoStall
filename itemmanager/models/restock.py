from django.db import models
from django.utils import timezone
from django.conf import settings

class RestockManager(models.Manager):
    pass


class Restock(models.Model):
    restock_PIC = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    restock_proof_of_payment = models.ImageField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    objects = RestockManager()

    def __str__(self):
        return super().__str__()
    
    @property
    def total_cost(self):
        from . import RestockItem
        cost = RestockItem.objects.restock_total_cost(restock=self)
        return cost