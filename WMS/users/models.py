from django.db import models

# Create your models here.
# -*- coding:utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.conf import settings
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    """
    员工
    """

    username = models.CharField(max_length=20, help_text=u"手机号", unique=True,
                                verbose_name=u"手机号")
    full_name = models.CharField(max_length=20, help_text=u"姓名", verbose_name=u"姓名", null=True, blank=True)
    id_number = models.CharField(max_length=45, unique=True, null=True, error_messages={"unique": u"此成员已存在"},
                                 blank=True, help_text=u"身份证号码", verbose_name=u"身份证号码")

    address = models.CharField(max_length=100, null=True, help_text=u'家庭住址', verbose_name=u'家庭住址')
    status = models.SmallIntegerField(default=1, help_text=u'状态', verbose_name=u'状态',
                                      choices=((0, u"已经离职"), (1, u"在职")))
    position = models.SmallIntegerField(default=0, help_text=u'职务', verbose_name=u'职务',
                                        choices=((0, "普通员工"), (1, '组长')))
    entry_date = models.DateTimeField(default=timezone.now, help_text=u"入职时间", verbose_name=u"入职时间")
    leaving_date = models.DateTimeField(default=None, null=True, blank=True, help_text=u'离职时间', verbose_name=u"离职时间")

    group = models.SmallIntegerField(default=0)

    is_staff = models.BooleanField(default=False, help_text=u"用户是否能登录后台管理系统", verbose_name=u"是否登录后台")
    is_active = models.BooleanField(default=False, help_text=u"是否有效", verbose_name=u"是否有效", choices=(
        (True, '有效客户'),
        (False, '无效客户'),
    ))

    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        app_label = "users"
        db_table = "users"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def get_full_name(self):
        return "{} -- {}".format(self.username, self.full_name)

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

# class UserGroup(models.Model):
#     """
#     部门
#     """
#     name = models.CharField(max_length=15, unique=True, help_text=u'部门', verbose_name=u'部门')
#     contained_max = models.IntegerField(default=30, help_text=u'最大可容纳人数', verbose_name=u'最大可容纳人数')
#     create_date = models.DateTimeField(default=timezone.now, help_text=u"成立时间", null=True, verbose_name=u"成立时间")
#     principal = models.CharField(max_length=10, help_text=u'负责人', verbose_name=u'负责人')
#     address = models.CharField(max_length=20, help_text=u'部门地址', verbose_name=u'部门地址')
#     phone = models.CharField(max_length=20, help_text=u'部门电话', verbose_name=u'部门电话')
#     flag = models.SmallIntegerField(default=0)
#
#     class Meta:
#         app_label = "users"
#         db_table = "users_group"
#         verbose_name = "部门"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
#
#     def __unicode__(self):
#         return self.name
