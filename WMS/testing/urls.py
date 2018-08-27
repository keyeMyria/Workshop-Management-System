# -*- coding:utf-8 -*-
from django.urls import path
from .views import get_token_callback, get_token, osscallback, ossimageupload

app_name = 'wechat'
urlpatterns = [

    path('ossupload', ossimageupload),
    path('get_token/', get_token, name='gettoken'),
    path('osscallback/', osscallback, name='osscallback'),
]
