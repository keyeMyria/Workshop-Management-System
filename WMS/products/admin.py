#-*- coding:utf-8 -*-
from django.contrib import admin

from base.admin import CustomAdmin
from .models import Product, ProductCategory

@admin.register(Product)
class ProductAdmin(CustomAdmin):
    list_display = ['pro_num_name', 'describe', 'cj_price', 'fr_price', 'yt_price', 'bz_price', 'status', 'category']
    search_fields = ['pro_num', 'name', 'status']
    list_filter = ['category','status']

    def pro_num_name(self, obj):
        return "{0} -- {1}".format(obj.pro_num, obj.name)

    pro_num_name.short_description = u'产品编号/名称'

@admin.register(ProductCategory)
class ProductCategoryAdmin(CustomAdmin):
    list_display = ['name', 'remark']
    search_fields = ['name', 'remark']

