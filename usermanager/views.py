from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from baseapp.decorators import admin_required
from baseapp.models import *

from collections import defaultdict
import math


class UserListView(TemplateView):
    model = TSUser
    template_name = 'user_list.html'

    def get_context_data(self, *args, **kwargs):
        pagination = kwargs.get('page')
        request = kwargs.get('request')
        try:
            pagination = max(0, int(pagination) - 1)
        except ValueError:
            pagination = 0
        pagination = pagination if pagination > 0 else 0
        users_per_page = 5
        users = TSUser.objects.order_by('user__first_name').order_by('user__last_name')
        max_pagination = math.ceil(users.count() / users_per_page)
        min_user_index = pagination*users_per_page
        context = {
            'ts_users': users[min_user_index:min_user_index+users_per_page],
            'paginations': range(1, max_pagination+1),
            'pagination': pagination + 1,
            'min_user_index': min_user_index,
            'active_tab': 'staff'
        }
        return context

    @method_decorator(admin_required)
    def get(self, request, *args, **kwargs):
        pagination = request.GET.get('p', '') or 1
        context = self.get_context_data(page=pagination, request=request)
        return render(request, self.template_name, context)

@admin_required
def user_detail(request):
    return render(request, 'core/construction.html', {'active_tab': 'staff'})

@admin_required
def user_new(request):
    return render(request, 'core/construction.html', {'active_tab': 'staff'})

@admin_required
def user_edit(request):
    return render(request, 'core/construction.html', {'active_tab': 'staff'})

@admin_required
def user_delete(request):
    return render(request, 'core/construction.html', {'active_tab': 'staff'})