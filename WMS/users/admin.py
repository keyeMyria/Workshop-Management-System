# -*- coding:utf-8 -*-

from django.contrib import admin
from django.conf import settings

from base.admin import CustomAdmin
from .models import User

@admin.register(User)
class UserAdmin(CustomAdmin):
    list_display = ['username', 'group', 'status', 'position', 'entry_date']
    search_fields = ['username']
    list_filter = ['status', 'group', 'position']
    readonly_fields = ['entry_date']


#
# @admin.register(UserGroup)
# class UserGroupAdmin(CustomAdmin):
#     fields = ['name', 'contained_max', 'principal', 'address', 'phone', 'create_date']
#     list_display = ['name', 'contained_max', 'principal', 'address', 'phone', 'create_date']
#     search_fields = ['name', 'principal', 'phone']
#     readonly_fields = ['create_date']
#     actions_on_bottom = False
#     actions_on_top = True
#
#

