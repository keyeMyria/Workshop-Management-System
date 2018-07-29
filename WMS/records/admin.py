# -*- coding:utf-8 -*-

from django.contrib import admin

from base.admin import CustomAdmin
from products.models import Warehouse, ProductBid
from salary.models import SalaryList
from .models import RecordTailor, RecordSew, RecordIron, RecordOutput
from users.models import User
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
        if not change:
            super(RecordTailorAdmin, self).save_model(request, obj, form, change)
            amount = obj.product.tailor_price * obj.number
            ProductBid.objects.create(remainingNumberSew=obj.number, remainingNumberIron=obj.number, recordTailor=obj, status_num=obj.number, number=obj.number)
            SalaryList.objects.create(user=obj.user, amount=amount, recordTailor=obj)
        else:
            super(RecordTailorAdmin, self).save_model(request, obj, form, change)
            # 更改产品标的
            productbid = ProductBid.objects.get(recordTailor=obj)
            num = obj.number - productbid.status_num
            productbid.remainingNumberSew += num
            productbid.remainingNumberIron += num
            productbid.number = obj.number
            productbid.status_num = obj.number
            productbid.save()
            # 更改工资记录
            salarylist = SalaryList.objects.get(recordTailor=obj)
            salarylist.user = obj.user
            salarylist.amount = obj.product.tailor_price * obj.number
            salarylist.save()


@admin.register(RecordSew)
class RecordSewAdmin(CustomAdmin):
    fields = ['user', ('productBid', 'number'), ('create_date', 'updated_datetime')]
    list_display = ['user', 'productBid', 'number', 'create_date', 'updated_datetime']
    search_fields = ['user__username', 'productBid', 'number']
    list_filter = []
    readonly_fields = ['create_date', 'updated_datetime']

    def save_model(self, request, obj, form, change):
        if not change:
            super(RecordSewAdmin, self).save_model(request, obj, form, change)
            obj.status_number = obj.number
            super(RecordSewAdmin, self).save_model(request, obj, form, change)
            obj.productBid.remainingNumberSew -= obj.number
            obj.productBid.save()
            amount = obj.productBid.recordTailor.product.sew_price * obj.number
            SalaryList.objects.create(user=obj.user, amount=amount, recordSew=obj)
        else:
            num = obj.status_number - obj.number

            obj.productBid.remainingNumberSew += num
            obj.productBid.save()
            obj.status_number = obj.number

            super(RecordSewAdmin, self).save_model(request, obj, form, change)
            amount = obj.productBid.recordTailor.product.sew_price * obj.number
            salarylist = SalaryList.objects.get(recordSew=obj)
            salarylist.user = obj.user
            salarylist.amount = amount
            salarylist.save()


@admin.register(RecordIron)
class RecordIronAdmin(CustomAdmin):
    fields = ['user', ('productBid', 'number'), ('create_date', 'updated_datetime')]
    list_display = ['user', 'productBid', 'number', 'create_date', 'updated_datetime']
    search_fields = ['user__username', 'productBid', 'number']
    list_filter = []
    readonly_fields = ['create_date', 'updated_datetime']

    def save_model(self, request, obj, form, change):
        amount = obj.productBid.recordTailor.product.iron_price * obj.number
        product = obj.productBid.recordTailor.product
        if not change:
            # 保存记录
            obj.status_number = obj.number
            super(RecordIronAdmin, self).save_model(request, obj, form, change)
            # 更新产品标剩余数量
            obj.productBid.remainingNumberIron -= obj.number
            obj.productBid.save()
            # 增加工资记录
            SalaryList.objects.create(user=obj.user, amount=amount, recordIron=obj)
            # 更新库存记录
            warehouses = Warehouse.objects.filter(product=product)
            if warehouses.exists():
                warehouse = warehouses[0]
                warehouse.number += obj.number
                warehouse.update("number")
            else:
                Warehouse.objects.create(product=product, number=obj.number)
        else:
            # 更新产品标剩余数量
            num = obj.status_number - obj.number
            obj.productBid.remainingNumberIron += num
            obj.productBid.save()
            # 保存记录
            obj.status_number = obj.number
            super(RecordIronAdmin, self).save_model(request, obj, form, change)
            # 更新工资记录
            salarylist = SalaryList.objects.get(recordIron=obj)
            salarylist.user = obj.user
            salarylist.amount = amount
            salarylist.save()
            # 更新库存记录
            warehouse = Warehouse.objects.get(product=product)
            warehouse.number -= num
            warehouse.save()
