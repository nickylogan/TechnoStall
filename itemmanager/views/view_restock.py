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

@admin_required
def restock_list(request):
    pass

@admin_required
def restock_new(request):
    pass

@admin_required
def restock_detail(request):
    pass

@admin_required
def restock_delete(request):
    pass