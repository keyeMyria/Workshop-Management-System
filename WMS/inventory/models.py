# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from employees.models import Employee
from products.models import Product


class InRecord(models.Model):
    '''
    入库记录
    '''
    # type = models.SmallIntegerField(default=0,choices=((0, u'入库'), (1, u'出库')), help_text=u'类型', verbose_name=u'类型')
    status_number = models.IntegerField(default=0, help_text=u'状态 / 已经入库数量', verbose_name=u'状态 / 已经入库数量')
    number = models.IntegerField(help_text=u'数量', verbose_name=u'数量')
    employee = models.ForeignKey('employees.Employee', help_text=u'姓名', verbose_name=u'姓名', on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", help_text=u'产品', verbose_name=u'产品', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now, help_text=u'时间', verbose_name=u'时间')
    updated_datetime = models.DateTimeField(auto_now=True, help_text=u'最后修改时间', verbose_name=u"最后修改时间")

    class Meta:
        app_label = "inventory"
        db_table = "inventory_in_record"
        verbose_name = u"入库管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0} -- {1}'.format(self.number, self.product)

    def __unicode__(self):
        return '{0} -- {1}'.format(self.number, self.product)


class OutRecord(models.Model):
    '''
    出库记录
    '''
    # type = models.SmallIntegerField(default=0,choices=((0, u'入库'), (1, u'出库')), help_text=u'类型', verbose_name=u'类型')
    status_number = models.IntegerField(default=0, help_text=u'状态 / 已经入库数量', verbose_name=u'状态 / 已经入库数量')
    number = models.IntegerField(help_text=u'数量', verbose_name=u'数量')
    # employee = models.ForeignKey('employees.Employee', help_text=u'姓名', verbose_name=u'姓名')
    product = models.ForeignKey("products.Product", help_text=u'产品', verbose_name=u'产品', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now, help_text=u'时间', verbose_name=u'时间')
    updated_datetime = models.DateTimeField(auto_now=True, help_text=u'最后修改时间', verbose_name=u"最后修改时间")

    class Meta:
        app_label = "inventory"
        db_table = "inventory_out_record"
        verbose_name = u"出库管理"
        verbose_name_plural = verbose_name


class Warehouse(models.Model):
    '''
    库存
    '''
    product = models.ForeignKey("products.Product", help_text=u'产品', verbose_name=u'产品', on_delete=models.CASCADE)
    number = models.IntegerField(help_text=u'库存数量', verbose_name=u'库存数量')
    updated_time = models.DateField(auto_now=True, help_text=u'最后更新时间', verbose_name=u'最后更新时间')

    class Meta:
        app_label = "inventory"
        db_table = "inventory_warehouse"
        verbose_name = u"仓库库存"
        verbose_name_plural = verbose_name
