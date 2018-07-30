# -*- coding:utf-8 -*-
from django.urls import path
from .views import vaildate

app_name = 'wechat'
urlpatterns = [
    path('vaildate/', vaildate, name='vailtate'),
]
