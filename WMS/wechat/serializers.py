# -*- coding:utf-8 -*-

import hashlib

from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class WechatValidateSerializer(serializers.Serializer):
    signature = serializers.CharField(max_length=100,help_text='加密签名')
    timestamp = serializers.CharField(max_length=100,help_text='时间戳')
    nonce = serializers.CharField(max_length=100,help_text='随机数')
    echostr = serializers.CharField(max_length=100, help_text=u"随机字符串")


    def validate(self, attrs):
        array = [attrs['timestamp'], attrs['nonce'],settings.WECHAT_TOKEN]
        array.sort()

        if hashlib.sha1(''.join(array)).hexdigest() != attrs['echostr']:
            raise ValidationError('验证失败')
        return attrs