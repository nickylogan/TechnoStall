from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from baseapp.decorators import admin_required
from itemmanager.models import *
from itemmanager.forms import RestockForm

import math

class RestockListView(TemplateView):
    model = Restock
    template_name = 'restock_list.html'

    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        pagination = request.GET.get('p', '') or 1
        try:
            pagination = int(pagination) - 1
        except ValueError:
            pagination = 0
        pagination = pagination if pagination > 0 else 0
        restocks_per_page = 10
        admin = request.session['ts_user']['is_admin']
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
        return render(request, self.template_name, context)

class RestockNewView(TemplateView):
    @method_decorator(admin_required)
    def post(self, request, *args, **kwargs):
        pass

    @method_decorator(admin_required)
    def post(self, request, *args, **kwargs):
        pass

class RestockDetailView(TemplateView):
    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        pass

class RestockDeleteView(TemplateView):
    @method_decorator(admin_required)
    def post(self, request, *args, **kwargs):
        pass