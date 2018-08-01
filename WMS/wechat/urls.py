# -*- coding:utf-8 -*-
from django.urls import path
from .views import WechatValidate

app_name = 'wechat'
urlpatterns = [
    path('validate', WechatValidate.as_view(), name='vailtate'),
]
