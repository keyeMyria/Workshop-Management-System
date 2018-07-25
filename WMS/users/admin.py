# -*- coding:utf-8 -*-

from django.contrib import admin
from django.conf import settings

from base.admin import CustomAdmin
from .models import User


@admin.register(User)
class UserAdmin(CustomAdmin):
    list_display = ['full_name', 'username', 'department', 'status', 'position', 'entry_date']
    search_fields = ['full_name', 'username', ]
    list_filter = ['status', 'department', 'position']
    readonly_fields = ['entry_date', 'leaving_date', 'last_login']

    fieldsets = [
        ('个人信息', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '个人基本信息',
            'fields': ('username', 'full_name', 'id_number', 'address', 'last_login')
        }),

        ('企业信息', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '',
            'fields': ('department', 'position', 'status', 'entry_date', 'leaving_date')
        }),
        ('系统权限', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '',
            'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions', 'groups')
        })
    ]

# @admin.register(UserGroup)
# class UserGroupAdmin(CustomAdmin):
#     fields = ['name', 'contained_max', 'principal', 'address', 'phone', 'create_date']
#     list_display = ['name', 'contained_max', 'principal', 'address', 'phone', 'create_date']
#     search_fields = ['name', 'principal', 'phone']
#     readonly_fields = ['create_date']
#     actions_on_bottom = False
#     actions_on_top = True
