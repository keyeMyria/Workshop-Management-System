# -*- coding:utf-8 -*-
from django.contrib import admin

from base.admin import CustomAdmin
from .models import Product, ProductCategory

from suit.sortables import SortableTabularInline, SortableModelAdmin, SortableStackedInline
from suit.admin import RelatedFieldAdmin, get_related_field


@admin.register(Product)
class ProductAdmin(CustomAdmin, RelatedFieldAdmin):
    list_display = ['pro_num_name', 'describe', 'cj_price', 'fr_price', 'yt_price', 'bz_price', 'status', 'category']
    search_fields = ['pro_num', 'name', 'status']
    list_filter = ['category', 'status']

    readonly_fields = ['created_datetime', 'updated_datetime']

    fieldsets = [
        ('产品信息', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '产品基本信息',
            'fields': ['pro_num', 'name', 'describe', 'category', 'status']}
         ),
        ('定价', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '在每个工序中的工人工资',
            'fields': ['cj_price', 'fr_price', 'yt_price', 'bz_price']}
         ),
        ('创建时间', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '该产品的创建时间',
            'fields': ['created_datetime', 'updated_datetime']}
         ),
    ]

    def pro_num_name(self, obj):
        return "{0} -- {1}".format(obj.pro_num, obj.name)

    pro_num_name.short_description = u'产品编号/名称'


@admin.register(ProductCategory)
class ProductCategoryAdmin(CustomAdmin):
    list_display = ['name', 'remark']
    search_fields = ['name', 'remark']
