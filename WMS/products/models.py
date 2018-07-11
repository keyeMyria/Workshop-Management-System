from django.db import models

# -*- coding:utf-8 -*-

from decimal import Decimal

from django.db import models
from django.utils import timezone


class Product(models.Model):
    '''
    产品
    '''
    pro_num = models.CharField(max_length=6, help_text=u'产品编号', verbose_name=u'产品编号')
    name = models.CharField(max_length=50, help_text=u"产品名称", verbose_name=u"产品名称")
    describe = models.CharField(max_length=50, null=True, blank=True, help_text=u"产品描述", verbose_name=u"产品描述")
    cj_price = models.DecimalField(default=Decimal(0.00), max_digits=20, decimal_places=2, help_text=u"裁剪价格", verbose_name=u"裁剪价格")
    fr_price = models.DecimalField(default=Decimal(0.00), max_digits=20, decimal_places=2, help_text=u"缝纫价格", verbose_name=u"缝纫价格")
    yt_price = models.DecimalField(default=Decimal(0.00), max_digits=20, decimal_places=2, help_text=u"熨烫价格", verbose_name=u"熨烫价格")
    bz_price = models.DecimalField(default=Decimal(0.00), max_digits=20, decimal_places=2, help_text=u"包装价格", verbose_name=u"包装价格")
    status = models.SmallIntegerField(default=0, help_text=u"0 未上市 1 热销中 2 已下市", verbose_name=u"状态", choices=((0, u'未上市'), (1, u'热销中'), (2, u'已下市')))
    created_datetime = models.DateTimeField(default=timezone.now, help_text=u"创建时间", verbose_name=u"创建时间")
    updated_datetime = models.DateTimeField(auto_now=True, help_text=u'更新时间', verbose_name=u"更新时间")
    category = models.ForeignKey('ProductCategory', help_text=u'分类', verbose_name=u"分类",on_delete=models.CASCADE)

    class Meta:
        app_label = "products"
        db_table = "products"
        verbose_name = u"产品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}-{1}".format(self.pro_num, self.name)

    def __unicode__(self):
        return "{0}-{1}".format(self.pro_num, self.name)


class ProductCategory(models.Model):
    '''
    产类分类
    '''
    name = models.CharField(max_length=12, help_text=u'分类', verbose_name=u'分类')
    remark = models.CharField(max_length=50, help_text=u"分类描述", verbose_name=u'分类描述')

    class Meta:
        app_label = "products"
        db_table = "product_category"
        verbose_name = u"产品分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

