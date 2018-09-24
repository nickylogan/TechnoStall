from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from baseapp.decorators import admin_required
from itemmanager.models import *
from itemmanager.forms import ItemForm

import math


class PricelistView(TemplateView):
    model = Item
    template_name = 'pricelist.html'

    def get_context_data(self, *args, **kwargs):
        filter_pattern = kwargs.get('filter')
        pagination = kwargs.get('page')
        try:
            pagination = int(pagination) - 1
        except ValueError:
            pagination = 0
        pagination = pagination if pagination > 0 else 0
        item_per_page = 10
        items = Item.objects.order_by('item_name').filter(item_name__icontains=filter_pattern)
        max_pagination = math.ceil(items.count() / item_per_page)
        min_item_index = pagination*item_per_page
        context = {
            'items': items[min_item_index:min_item_index+item_per_page],
            'paginations': range(1, max_pagination+1),
            'pagination': pagination + 1,
            'min_item_index': min_item_index,
            'filter_pattern': filter_pattern,
            'active_tab': 'item'
        }
        return context

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        filter_pattern = request.GET.get('f', '') or ''
        pagination = request.GET.get('p', '') or 1
        context = self.get_context_data(filter=filter_pattern, page=pagination)
        return render(request, self.template_name, context)


class ItemDetailView(TemplateView):
    model = Item
    template_name = 'item_detail.html'

    def get_context_data(self, *args, **kwargs):
        item = kwargs.get('item')
        restocks = RestockItem.objects.filter(
            item=item).order_by('-restock__date_created')
        context = {
            'item': item,
            'restock': restocks[0] if restocks else None,
            'active_tab': 'item'
        }
        return context

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs.get('pk'))
        context = self.get_context_data(item=item)
        return render(request, self.template_name, context)


class ItemNewView(TemplateView):
    model = Item
    template_name = 'item_edit.html'

    @method_decorator(admin_required)
    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            notice = "Item %s was successfully created" % item.item_name
            messages.success(request, notice, extra_tags='green rounded')    
            return redirect('item_detail', pk=item.pk)
        else:
            context = {'form': form, 'active_tab': 'item'}
            return render(request, self.template_name, context)

    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        form = ItemForm()
        context = {'form': form, 'active_tab': 'item'}
        return render(request, self.template_name, context)


class ItemEditView(TemplateView):
    model = Item
    template_name = 'item_edit.html'

    @method_decorator(admin_required)
    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs.get('pk'))
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            notice = "Item %s was successfully changed" % item.item_name
            messages.success(request, notice, extra_tags='green rounded')
            return redirect('item_detail', pk=item.pk)
        else:
            context = {'form': form, 'active_tab': 'item'}
            return render(request, self.template_name, context)

    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs.get('pk'))
        form = ItemForm(instance=item)
        context = {'form': form, 'item_pk': item.pk, 'active_tab': 'item'}
        return render(request, self.template_name, context)


class ItemDeleteView(TemplateView):
    model = Item

    @method_decorator(admin_required)
    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs.get('pk'))
        notice = "Item %s was successfully deleted" % item.item_name
        item.delete()
        messages.success(request, notice, extra_tags='green rounded')
        return redirect('pricelist')

    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs.get('pk'))
        return redirect('item_detail', pk=item.pk)
