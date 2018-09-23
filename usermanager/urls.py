from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('user/new/', views.user_new, name='user_new'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete', views.user_delete, name='user_delete'),
]