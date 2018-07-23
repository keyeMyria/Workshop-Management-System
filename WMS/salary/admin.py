# -*- coding:utf-8 -*-
from django.contrib import admin

from base.admin import CustomAdmin
from .models import Salary, SalaryList


class SalaryListAdmin(CustomAdmin):
    fileds = ['user', 'user_group', 'product', 'number', 'amount', 'create_date', 'status']
    list_display = ['user', 'user_group', 'product', 'number', 'amount', 'create_date', 'status']
    search_fields = ['user', 'amount']
    list_filter = ['user', 'amount', 'create_date', 'status']
    readonly_fields = ['user', 'user_group', 'product', 'number', 'amount', 'create_date', 'status', 'inrecord']
    ordering = ['-create_date']
    list_display_links = []

    def user_group(self, obj):
        return obj.inrecord.user.group

    def product(self, obj):
        return obj.inrecord.product

    def number(self, obj):
        return obj.inrecord.number

    user_group.short_description = u'部门'
    product.short_description = u'产品'
    number.short_description = u'数量'


class SalaryAdmin(CustomAdmin):
    list_display = ['month', 'user', 'amount', 'status']
    search_fields = ['user', 'amount']
    list_filter = ['user', 'amount', 'month', 'status']
    list_display_links = ['user']
    readonly_fields = ['user', 'amount', 'month', ]
    ordering = ['-month', 'user']
    list_editable = ['status']


admin.site.register(Salary, SalaryAdmin)
admin.site.register(SalaryList, SalaryListAdmin)
