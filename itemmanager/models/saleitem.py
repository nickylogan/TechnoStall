from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from . import Item, Sale


class SaleItemManager(models.Manager):
    def sale_total_amount(self, item):
        return super().get_queryset().filter(item=item).aggregate(models.Sum('sale_amount'))['sale_amount__sum'] or 0


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    sale_amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    sale_price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(1)])

    objects = SaleItemManager()

    class Meta:
        unique_together = (("sale", "item"))

    def __str__(self):
        return "%d %s(s) for %d" % (self.item.item_name, self.sale_amount, self.sale_price)

    def clean(self):
        errors = {}
        if self.item.item_availability == False:
            errors['item'] = ValidationError(
                _('Item not available!'), code='invalid')
        if self.sale_amount > self.item.item_stock:
            errors['sale_amount'] = ValidationError(
                _('Ensure sale amount is less or equal to item stock')
            )
        if errors:
            raise ValidationError(errors)
