from django.db import models
from django.utils import timezone

class RestockManager(models.Manager):
    pass


class Restock(models.Model):
    restock_PIC = models.CharField(max_length=50)
    restock_proof_of_payment = models.ImageField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    objects = RestockManager()

    def __str__(self):
        return super().__str__()