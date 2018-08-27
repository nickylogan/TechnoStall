from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('pricelist/', views.PricelistView.as_view() , name='pricelist'),
    path('items/new/', views.ItemNewView.as_view(), name='item_new'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('items/<int:pk>/edit', views.ItemEditView.as_view(), name='item_edit'),
    path('items/<int:pk>/delete', views.ItemDeleteView.as_view(), name='item_delete'),
    path('sales/', views.SaleListView.as_view(), name='sale_list'),
    path('sales/new/', views.SaleNewView.as_view(), name='sale_new'),
    path('sales/<int:pk>/', views.SaleDetailView.as_view(), name='sale_detail'),
    path('sales/<int:pk>/delete', views.SaleDeleteView.as_view(), name='sale_delete'),
    path('restocks/', views.RestockListView.as_view(), name='restock_list'),
    path('restocks/new/', views.RestockNewView.as_view(), name='restock_new'),
    path('restocks/<int:pk>/', views.RestockDetailView.as_view(), name='restock_detail'),
    path('restocks/<int:pk>/delete', views.RestockDeleteView.as_view(), name='restock_delete'),
]