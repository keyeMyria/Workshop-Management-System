# -*- coding:utf-8 -*-

from django.contrib import admin
from django.conf import settings

from .models import Employee, EmployeeGroup


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['username', 'group', 'phone', 'status', 'position', 'entry_date']
    search_fields = ['username', 'phone']
    list_filter = ['status', 'group', 'position']
    readonly_fields = ['entry_date']


class EmployeeGroupAdmin(admin.ModelAdmin):
    fields = ['name', 'contained_max', 'principal', 'address', 'phone', 'create_date']
    list_display = ['name', 'contained_max', 'principal', 'address', 'phone', 'create_date']
    search_fields = ['name', 'principal', 'phone']
    readonly_fields = ['create_date']

    def save_model(self, request, obj, form, change):
        obj.flag = settings.EMPLOYEE_GROUP.get(obj.name)
        obj.save()



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeGroup, EmployeeGroupAdmin)
