# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.db import models
from django.utils import timezone

from users.models import User


class SalaryList(models.Model):
    '''
    工资
    '''
    user = models.ForeignKey("users.User", help_text=u'姓名', verbose_name=u'姓名', on_delete=models.CASCADE)
    amount = models.DecimalField(default=Decimal(0.00), max_digits=20, decimal_places=2, help_text=u'金额',
                                 verbose_name=u'金额')
    create_date = models.DateTimeField(default=timezone.now, help_text=u'时间', verbose_name=u'时间')

    recordtailor = models.ForeignKey('records.RecordTailor', null=True, blank=True, on_delete=models.CASCADE, help_text=u'关联记录', verbose_name=u'关联记录')
    recordsew = models.ForeignKey('records.RecordSew', null=True, blank=True, on_delete=models.CASCADE, help_text=u'关联记录', verbose_name=u'关联记录')
    recordiron = models.ForeignKey('records.RecordIron', null=True, blank=True, on_delete=models.CASCADE, help_text=u'关联记录', verbose_name=u'关联记录')

    status = models.SmallIntegerField(default=0, verbose_name=u'状态', help_text=u'状态',
                                      choices=((0, u'未统计'), (1, u'已统计'),))

    class Meta:
        app_label = "salary"
        db_table = "salary_list"
        verbose_name = u"工资记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Salary(models.Model):
    user = models.ForeignKey('users.User', verbose_name=u'员工', help_text=u'员工', on_delete=models.CASCADE)
    amount = models.DecimalField(default=Decimal('0.00'), max_digits=20, decimal_places=2, verbose_name=u'月薪资',
                                 help_text=u'月薪资')
    month = models.CharField(max_length=10, verbose_name=u'月份', help_text=u'月份')
    status = models.SmallIntegerField(default=0, choices=((0, '未发放'), (1, '已发放'),), verbose_name=u'状态', help_text=u'状态')

    class Meta:
        app_label = "salary"
        db_table = "salary"
        verbose_name = u"应发工资"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
