#-*- coding:utf-8 -*-
from django.contrib import admin


from .models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pro_num_name', 'describe', 'cj_price', 'fr_price', 'yt_price', 'bz_price', 'status', 'category']
    search_fields = ['pro_num', 'name', 'status']
    list_filter = ['cj_price', 'fr_price', 'yt_price', 'bz_price', 'status']

    def pro_num_name(self, obj):
        return "{0} -- {1}".format(obj.pro_num, obj.name)

    pro_num_name.short_description = u'产品编号/名称'


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'remark']
    search_fields = ['name', 'remark']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)

