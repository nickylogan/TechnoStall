from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from baseapp.decorators import admin_required
from itemmanager.models import Item
import math

@login_required
def pricelist(request):
    filter_pattern = request.GET.get('f', '') or ''
    pagination = request.GET.get('p', '') or 1
    try:
        pagination = int(pagination) - 1
    except ValueError:
        pagination = 0
    pagination = pagination if pagination > 0 else 0
    item_per_page = 10
    items = Item.objects.order_by('item_name').filter(item_name__contains=filter_pattern)
    max_pagination = math.ceil(items.count() / item_per_page)
    min_item_index = pagination*item_per_page
    return render(request, 'pricelist.html', {
        'items': items[min_item_index:min_item_index+item_per_page], 
        'paginations': range(1,max_pagination+1),
        'pagination': pagination + 1,
        'min_item_index': min_item_index,
        'filter_pattern': filter_pattern,
        'active_tab': 'item'
        })

@login_required
def item_detail(request, pk):
    pass

@admin_required
def item_new(request):
    pass

@admin_required
def item_edit(request):
    pass

@admin_required
def restock_list(request):
    pass

@admin_required
def restock_edit(request):
    pass

@admin_required
def restock_new(request):
    pass

@admin_required
def restock_detail(request):
    pass

@login_required
def sale_list(request):
    pass

@login_required
def sale_new(request):
    pass

@login_required
def sale_detail(request):
    pass

@admin_required
def sale_edit(request):
    pass

