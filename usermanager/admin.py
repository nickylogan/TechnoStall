from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *


class TSUserInline(admin.StackedInline):
    model = TSUser
    can_delete = False
    verbose_name_plural = 'Technostall User'


class UserAdmin(BaseUserAdmin):
    inlines = (TSUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
