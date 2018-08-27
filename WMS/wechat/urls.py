# -*- coding:utf-8 -*-
from django.urls import path
from .views import WechatValidateView

app_name = 'wechat'

urlpatterns = [
    path('validate/', WechatValidateView.as_view(), name='vailtate'),
]
