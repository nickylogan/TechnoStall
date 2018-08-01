from django.contrib import admin
from .models import Item, Restock, Sale

# Register your models here.
admin.site.register(Item)
admin.site.register(Restock)
admin.site.register(Sale)