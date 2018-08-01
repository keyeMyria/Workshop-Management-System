# -*- coding:utf-8 -*-
from django.urls import path
from .views import WechatValidate

app_name = 'wechat'
urlpatterns = [
    path('vaildate/', WechatValidate.as_view(), name='vailtate'),
]
