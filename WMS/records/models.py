# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from users.models import User
from products.models import Product


class RecordTailor(models.Model):
    status_number = models.IntegerField(default=0, help_text=u'上次记录', verbose_name=u'上次记录')
    number = models.IntegerField(help_text=u'数量', verbose_name=u'数量')
    user = models.ForeignKey('users.User', help_text=u'姓名', verbose_name=u'姓名', on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", help_text=u'产品', verbose_name=u'产品', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now, help_text=u'时间', verbose_name=u'时间')
    updated_datetime = models.DateTimeField(auto_now=True, help_text=u'最后修改时间', verbose_name=u"最后修改时间")

    class Meta:
        app_label = 'records'
        db_table = 'records_tailor'
        verbose_name = u"裁剪记工"
        verbose_name_plural = verbose_name


class RecordSew(models.Model):
    '''
    缝纫记工
    '''
    status_number = models.IntegerField(default=0, help_text=u'状态 / 已经入库数量', verbose_name=u'状态 / 已经入库数量')
    number = models.IntegerField(help_text=u'数量', verbose_name=u'数量')
    user = models.ForeignKey('users.User', help_text=u'姓名', verbose_name=u'姓名', on_delete=models.CASCADE)
    productBid = models.ForeignKey("products.ProductBid", help_text=u'产品', verbose_name=u'产品', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now, help_text=u'时间', verbose_name=u'时间')
    updated_datetime = models.DateTimeField(auto_now=True, help_text=u'最后修改时间', verbose_name=u"最后修改时间")

    class Meta:
        app_label = "records"
        db_table = "records_sew"
        verbose_name = u"缝纫记工"
        verbose_name_plural = verbose_name


class RecordIron(models.Model):
    '''
    入库记录：熨烫组
    '''
    status_number = models.IntegerField(default=0, help_text=u'状态 / 已经入库数量', verbose_name=u'状态 / 已经入库数量')
    number = models.IntegerField(help_text=u'数量', verbose_name=u'数量')
    user = models.ForeignKey('users.User', help_text=u'姓名', verbose_name=u'姓名', on_delete=models.CASCADE)
    productBid = models.ForeignKey("products.ProductBid", help_text=u'产品', verbose_name=u'产品', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now, help_text=u'时间', verbose_name=u'时间')
    updated_datetime = models.DateTimeField(auto_now=True, help_text=u'最后修改时间', verbose_name=u"最后修改时间")

    class Meta:
        app_label = "records"
        db_table = "records_iron"
        verbose_name = u"熨烫记工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0} -- {1}'.format(self.number, self.productBid.recordTailor.product.name)

    def __unicode__(self):
        return '{0} -- {1}'.format(self.number, self.productBid.recordTailor.product.name)


class RecordOutput(models.Model):
    '''
    出库记录
    '''
    status_number = models.IntegerField(default=0, help_text=u'状态 / 已经入库数量', verbose_name=u'状态 / 已经入库数量')
    number = models.IntegerField(help_text=u'数量', verbose_name=u'数量')
    # employee = models.ForeignKey('employees.Employee', help_text=u'姓名', verbose_name=u'姓名')
    product = models.ForeignKey("products.Product", help_text=u'产品', verbose_name=u'产品', on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now, help_text=u'时间', verbose_name=u'时间')
    updated_datetime = models.DateTimeField(auto_now=True, help_text=u'最后修改时间', verbose_name=u"最后修改时间")

    class Meta:
        app_label = "records"
        db_table = "records_output"
        verbose_name = u"出库记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s - %s 件" % (self.product.name, self.number)

    def __unicode__(self):
        return "%s - %s 件" % (self.product.name, self.number)
