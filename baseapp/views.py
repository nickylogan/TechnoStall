from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import TSUser

def index(request):
    return render(request, 'core/index.html')

def login(request):
    if request.POST:
        auth_logout(request)
        username = password = ''
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            tsuser = TSUser.objects.get_user(user=user)
            request.session['ts_user'] = {}
            request.session['ts_user']['major'] = tsuser.major_string()
            request.session['ts_user']['role'] = tsuser.role_string()
            request.session['ts_user']['major_short'] = tsuser.major
            request.session['ts_user']['role_short'] = tsuser.role
            request.session['ts_user']['is_admin'] = tsuser.is_admin()
            
            auth_login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'core/login.html', {'error': True})
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        return render(request, 'core/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required(login_url='/login')
def profile(request):
    # TODO create profile template
    return render(request, 'core/dashboard.html')

def print(request):
    return render(request, 'core/construction.html', {'active_tab': 'print'})