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

class SaleListView(TemplateView):
    model = Sale
    template_name = 'sale_list.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pagination = request.GET.get('p', '') or 1
        try:
            pagination = int(pagination) - 1
        except ValueError:
            pagination = 0
        pagination = pagination if pagination > 0 else 0
        sales_per_page = 10
        admin = request.session['ts_user']['is_admin']
        sales = Sale.objects.order_by('-date_created')
        if not admin: sales = sales.filter(user_on_duty=request.user)
        max_pagination = math.ceil(sales.count() / sales_per_page)
        min_sale_index = pagination*sales_per_page
        return render(request, self.template_name, {
            'sales': sales[min_sale_index:min_sale_index+sales_per_page], 
            'paginations': range(1,max_pagination+1),
            'pagination': pagination + 1,
            'min_sale_index': min_sale_index,
            'active_tab': 'sale'
            })

@login_required
def sale_new(request):
    items = Item.objects.all()
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('post_detail', pk=post.pk)
    # else:
    #     form = PostForm()
    return render(request, 'sale_new.html', {'items': items})

@login_required
def sale_detail(request):
    pass

@admin_required
def sale_delete(request):
    pass