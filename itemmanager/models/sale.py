from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone

class SaleManager(models.Model):
    pass
    
class Sale(models.Model):
    user_on_duty = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(default=timezone.now)

    objects = SaleManager()

    def __str__(self):
        return super().__str__()