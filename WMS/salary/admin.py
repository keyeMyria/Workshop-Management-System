# -*- coding:utf-8 -*-
from django.contrib import admin

from django.urls import reverse
from django.utils.html import format_html

from base.admin import CustomAdmin
from .models import Salary, SalaryList


class SalaryListAdmin(CustomAdmin):

    list_display = ['department','user',  'product', 'number', 'amount', 'create_date', 'status','inrecord']
    search_fields = ['user', 'amount']
    list_filter = ['user', 'amount', 'create_date', 'status']
    ordering = ['-create_date']
    list_display_links = []

    def has_add_permission(self, request):
        return False

    def department(self, obj):
        return obj.inrecord.user.department

    def product(self, obj):
        return obj.inrecord.product

    def number(self, obj):
        return obj.inrecord.number

    def inrecord(self, obj):
        inrecord = obj.inrecord
        link = reverse("admin:inventory_inrecord_change", args=(inrecord.id,))
        a_text = "入库记录"
        return format_html('<a target="_blank" href="%s">%s</a>' % (link, a_text))


    department.short_description = u'部门'
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

    def has_add_permission(self, request):
        return False



admin.site.register(Salary, SalaryAdmin)
admin.site.register(SalaryList, SalaryListAdmin)
