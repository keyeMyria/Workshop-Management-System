# -*- coding:utf-8 -*-

from django.contrib import admin

from base.admin import CustomAdmin
from products.models import Warehouse
from .models import RecordTailor, RecordSew, RecordIron, RecordOutput
from .services import set_salary
from .forms import *


@admin.register(RecordOutput)
class OutRecordAdmin(CustomAdmin):
    fields = ['number', 'product', 'create_date']
    list_display = ['product', 'number', 'create_date', 'updated_datetime']
    search_fields = ['product__name', 'number']
    list_filter = ['product', 'create_date', 'updated_datetime']
    #
    # def save_model(self, request, obj, form, change):
    #
    #     if not change:
    #
    #         if obj.number == 0:
    #             pass
    #
    #         # 新建 出库记录
    #         ware = Warehouse.objects.filter(product=obj.product).first()
    #         if ware is None or ware.number < obj.number:
    #             # 抛出异常 库存不足
    #             # return '库存不足'
    #             pass
    #
    #         obj.status_number = obj.number
    #         obj.save()
    #         ware.number -= obj.number
    #         ware.save(update_fields=['number'])
    #     else:
    #         # 更新出库记录
    #         ware = Warehouse.objects.get(product=obj.product)
    #         if ware.number < obj.number:
    #             # 抛出异常 库存不足
    #             # return '库存不足'
    #             pass
    #         ware.number += obj.status_number
    #         ware.number -= obj.number
    #         obj.status_number = obj.number
    #         ware.save(update_fields=['number'])
    #         obj.save(update_fields=['status_number', 'number'])


@admin.register(RecordTailor)
class RecordTailorAdmin(CustomAdmin):
    fields = ['user', ('product', 'number'), ('create_date', 'updated_datetime')]
    list_display = ['user', 'product', 'number', 'create_date', 'updated_datetime']
    search_fields = ['user__username', 'product', 'number']
    list_filter = []
    readonly_fields = ['create_date', 'updated_datetime']

    def save_model(self, request, obj, form, change):
        from products.models import ProductBid
        from salary.models import SalaryList
        if not change:
            super(RecordTailorAdmin, self).save_model(request, obj, form, change)
            amount = obj.product.tailor_price * obj.number
            ProductBid.objects.create(remainingNumberSew=obj.number, remainingNumberIron=obj.number, recordTailor=obj)
            SalaryList.objects.create(user=obj.user, amount=amount,inrecord=obj.id)


@admin.register(RecordSew)
class RecordSewAdmin(CustomAdmin):
    fields = ['user', ('productBid', 'number'), ('create_date', 'updated_datetime')]
    list_display = ['user', 'productBid', 'number', 'create_date', 'updated_datetime']
    search_fields = ['user__username', 'productBid', 'number']
    list_filter = []
    readonly_fields = ['create_date', 'updated_datetime']


@admin.register(RecordIron)
class RecordIronAdmin(CustomAdmin):
    fields = ['user', ('productBid', 'number'), ('create_date', 'updated_datetime')]
    list_display = ['user', 'productBid', 'number', 'create_date', 'updated_datetime']
    search_fields = ['user__username', 'productBid', 'number']
    list_filter = []
    readonly_fields = ['create_date', 'updated_datetime']

    # def save_model(self, request, obj, form, change):
    #
    #     if obj.number == 0:
    #         # 抛出异常
    #         pass
    #     if not change:
    #         # 创建 入库 记录的操作
    #         # 更新记录
    #         obj.status_number = obj.number
    #         obj.save()
    #         # 更新库存
    #         ware = Warehouse.objects.filter(product=obj.product).first()
    #         if ware:
    #             ware.number += obj.number
    #         else:
    #             ware = Warehouse.objects.create(product=obj.product, number=obj.number)
    #         ware.save()
    #         # 更新工资记录
    #         set_salary(obj)
    #     else:
    #         # 更新 入库记录
    #         # 更新库存状态
    #         ware = Warehouse.objects.get(product=obj.product)
    #         ware.number -= obj.status_number
    #         ware.number += obj.number
    #         ware.save(update_fields=['number'])
    #         # 更新记录状态
    #         obj.status_number = obj.number
    #         obj.save(update_fields=['status_number', 'number'])
    #         # 更新工资记录
    #         set_salary(obj)
