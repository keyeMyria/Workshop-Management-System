# -*- coding:utf-8 -*-

from django.contrib import admin

from .models import Salary, SalaryList


class SalaryListAdmin(admin.ModelAdmin):
    fileds = ['employee', 'employee_group', 'product', 'number', 'amount', 'create_date', 'status']
    list_display = ['employee', 'employee_group', 'product', 'number', 'amount', 'create_date', 'status']
    search_fields = ['employee', 'amount']
    list_filter = ['employee', 'amount', 'create_date', 'status']
    readonly_fields = ['employee', 'employee_group', 'product', 'number', 'amount', 'create_date', 'status', 'inrecord']
    ordering = ['-create_date']
    list_display_links = []

    def employee_group(self, obj):
        return obj.inrecord.employee.group

    def product(self, obj):
        return obj.inrecord.product

    def number(self, obj):
        return obj.inrecord.number

    employee_group.short_description = u'部门'
    product.short_description = u'产品'
    number.short_description = u'数量'


class SalaryAdmin(admin.ModelAdmin):
    list_display = ['month', 'employee', 'amount', 'status']
    search_fields = ['employee', 'amount']
    list_filter = ['employee', 'amount', 'month', 'status']
    list_display_links = ['employee']
    readonly_fields = ['employee', 'amount', 'month', ]
    ordering = ['-month', 'employee']
    list_editable = ['status']


admin.site.register(Salary, SalaryAdmin)
admin.site.register(SalaryList, SalaryListAdmin)
