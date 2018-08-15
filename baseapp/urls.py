from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile', views.profile, name='profile'),
    path('dashboard/', include('itemmanager.urls')),
    path('', views.index, name='index')
]
