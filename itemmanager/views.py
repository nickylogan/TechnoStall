from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from baseapp.decorators import admin_required
from itemmanager.models import Item

@login_required
def pricelist(request):
    pass

@login_required
def item_detail(request):
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

