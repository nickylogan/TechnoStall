from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from baseapp.decorators import admin_required
from itemmanager.models import *
from itemmanager.forms import RestockForm, RestockItemForm, BaseRestockItemFormSet

from collections import defaultdict
import math

class RestockListView(TemplateView):
    model = Restock
    template_name = 'restock_list.html'

    def get_context_data(self, *args, **kwargs):
        pagination = kwargs.get('page')
        try:
            pagination = int(pagination) - 1
        except ValueError:
            pagination = 0
        pagination = pagination if pagination > 0 else 0
        restocks_per_page = 10
        restocks = Restock.objects.order_by('-date_created')
        max_pagination = math.ceil(restocks.count() / restocks_per_page)
        min_restock_index = pagination*restocks_per_page
        context = {
            'restocks': restocks[min_restock_index:min_restock_index+restocks_per_page],
            'paginations': range(1, max_pagination+1),
            'pagination': pagination + 1,
            'min_restock_index': min_restock_index,
            'active_tab': 'restock'
        }
        return context

    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        pagination = request.GET.get('p', '') or 1
        context = self.get_context_data(page=pagination)        
        return render(request, self.template_name, context)

class RestockNewView(TemplateView):
    template_name = 'restock_new.html'
    RestockItemFormSet = formset_factory(
            RestockItemForm, formset=BaseRestockItemFormSet)

    def get_context_data(self, *args, **kwargs):
        context = {
            'restockitem_formset': kwargs.get('formset'),
            'restock_form': kwargs.get('form'),
            'active_tab': 'restock'
        }
        return context

    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        restock_form = RestockForm()
        restockitem_formset = self.RestockItemFormSet()

        context = self.get_context_data(formset=restockitem_formset, form=restock_form)
        return render(request, self.template_name, context)

    @method_decorator(admin_required)
    def post(self, request, *args, **kwargs):
        restock_form = RestockForm(request.POST, request.FILES)
        restockitem_formset = self.RestockItemFormSet(request.POST)
        print(request.POST)
        print(restockitem_formset.is_valid())
        if restock_form.is_valid() and restockitem_formset.is_valid():
            # Create restock
            proof = restock_form.cleaned_data.get('restock_proof_of_payment')

            restock = Restock(restock_PIC=request.user, restock_proof_of_payment=proof)
            restock.save()

            # Make unique
            restock_items = []
            restock_quantities = defaultdict(int)
            restock_costs = defaultdict(float)
            for restockitem_form in restockitem_formset:
                item_pk = restockitem_form.cleaned_data.get('item')
                quantity = restockitem_form.cleaned_data.get('quantity')
                cost = restockitem_form.cleaned_data.get('cost')
                item = Item.objects.get(pk=item_pk)
                print(item, quantity, cost)
                restock_items.append(item)
                restock_quantities[item] += quantity
                restock_costs[item] += cost

            # Save all restockitems
            for item in restock_items:
                quantity = restock_quantities[item]
                cost = restock_costs[item]
                restock_item = RestockItem(restock=restock, item=item, restock_item_amount=quantity, restock_item_total_cost=cost)
                restock_item.save()
            
            notice = "Restock was successfully created"
            messages.success(request, notice, extra_tags='green rounded')
            return redirect('restock_detail', pk=restock.pk)
        else:
            context = self.get_context_data(formset=restockitem_formset, form=restock_form)
            return render(request, self.template_name, context)

    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        RestockItemFormSet = formset_factory(
            RestockItemForm, formset=BaseRestockItemFormSet)
        restockitem_formset = RestockItemFormSet()
        context = self.get_context_data(formset=restockitem_formset)
        return render(request, self.template_name, context)

class RestockDetailView(TemplateView):
    model = Restock
    template_name = 'restock_detail.html'

    def get_context_data(self, *args, **kwargs):
        restock = kwargs.get('restock')
        restockitems = RestockItem.objects.filter(restock=restock).order_by('item__item_name')
        context = {
            'restock': restock,
            'restockitems': restockitems,
            'active_tab': 'restock'
        }
        return context

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        restock = get_object_or_404(Restock, pk=self.kwargs.get('pk'))
        context = self.get_context_data(restock=restock)
        return render(request, self.template_name, context)

class RestockDeleteView(TemplateView):
    @method_decorator(admin_required)
    def post(self, request, *args, **kwargs):
        pass