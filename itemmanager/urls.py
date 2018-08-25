from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('pricelist/', views.PricelistView.as_view() , name='pricelist'),
    path('items/new/', views.ItemNewView.as_view(), name='item_new'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('items/<int:pk>/edit', views.ItemEditView.as_view(), name='item_edit'),
    path('items/<int:pk>/delete', views.item_delete, name='item_delete'),
    path('sales/', views.SaleListView.as_view(), name='sale_list'),
    path('sales/new/', views.sale_new, name='sale_new'),
    path('sales/<int:pk>/', views.sale_detail, name='sale_detail'),
    path('sales/<int:pk>/delete', views.sale_delete, name='sale_delete'),
    path('restocks/', views.restock_list, name='restock_list'),
    path('restocks/new/', views.restock_new, name='restock_new'),
    path('restocks/<int:pk>/', views.restock_detail, name='restock_detail'),
    path('restocks/<int:pk>/delete', views.restock_delete, name='restock_delete'),
]