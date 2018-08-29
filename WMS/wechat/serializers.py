# -*- coding:utf-8 -*-

import hashlib
import json

from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class WechatValidateSerializer(serializers.Serializer):
    """
    验证微信消息源
    """
    signature = serializers.CharField(max_length=100, help_text=u"微信加密签名")
    timestamp = serializers.CharField(max_length=100, help_text=u"时间戳")
    nonce = serializers.CharField(max_length=100, help_text=u"随机数")
    echostr = serializers.CharField(max_length=100, help_text=u"随机字符串")

    def validate(self, attrs):
        items = [attrs['nonce'], attrs['timestamp'], settings.WECHAT_TOKEN]
        items.sort()
        #hashlib.sha1(attrs['nonce'].encode('utf8'))
        #hashlib.sha1(attrs['timestamp'].encode('utf8'))
        #hashlib.sha1(settings.WECHAT_TOKEN.encode('utf8'))
        if hashlib.sha1(''.join(items)).hexdigest() != attrs['signature']:
            raise ValidationError("签名验证失败")
        return attrs


