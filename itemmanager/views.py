from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from baseapp.decorators import admin_required
from itemmanager.models import Item, Restock, RestockItem
from itemmanager.forms import ItemForm
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
    item = get_object_or_404(Item, pk=pk)
    restocks = RestockItem.objects.filter(item=item).order_by('-restock__date_created')
    return render(request, 'item_detail.html', {
        'item': item,
        'restock': restocks[0] if restocks else None
        })

@admin_required
def item_new(request):
    pass

@admin_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
        return render(request, 'item_edit.html', {'form': form, 'item_pk': item.pk})

@admin_required
def item_delete(request, pk):
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

