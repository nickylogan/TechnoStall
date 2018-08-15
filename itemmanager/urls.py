from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('pricelist/', views.pricelist, name='item_list'),
    path('items/new/', views.item_new, name='item_new'),
    path('items/<int:pk>', views.item_detail, name='item_detail'),
    path('items/<int:pk>/edit', views.item_edit, name='item_edit'),
]