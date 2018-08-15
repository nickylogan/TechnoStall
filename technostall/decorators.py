from functools import update_wrapper, wraps
from django.http import HttpResponseNotFound, HttpResponseForbidden, Http404
from django.utils.decorators import available_attrs
from baseapp.models import TSUser

def admin_required(function=None):
    def check_admin(user):
        if user and user.is_authenticated:
            ts_user = TSUser.objects.get_user(user)
            if ts_user:
                return ts_user.is_admin()
            else:
                return False
        else:
            return False

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if check_admin(request.user):
                return view_func(request, *args, **kwargs)
            else:
                raise Http404
        return wraps(view_func, assigned=available_attrs(view_func))(_wrapped_view)

    if function is None:
        return decorator
    else:
        return decorator(function)