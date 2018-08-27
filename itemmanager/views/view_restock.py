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
    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        pass

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