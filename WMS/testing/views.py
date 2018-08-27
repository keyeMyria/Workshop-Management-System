# -*- coding:utf-8 -*-

import time
import datetime
import json
import base64
import hmac
from hashlib import sha1 as sha

from django.shortcuts import render
from django.http import HttpResponse

accessKeyId = 'LTAIQnEddLS1IMjz'
accessKeySecret = 'WNt7l32Lr8jg6pRGYmKnXfhZyYgvma'
host = 'http://d-dolphin.oss-cn-shanghai.aliyuncs.com'
expire_time = 60
upload_dir = ''
callback_url = "http://oss-demo.aliyuncs.com:23450"

def get_iso_8601(expire):
    gmt = datetime.datetime.utcfromtimestamp(expire).isoformat()
    gmt += 'Z'
    return gmt

def get_token_callback(request):
    now = int(time.time())
    expire_syncpoint  = now + expire_time
    expire = get_iso_8601(expire_syncpoint)

    policy_dict = {}
    policy_dict['expiration'] = expire
    condition_array = []
    array_item = []
    array_item.append('starts-with')
    array_item.append('$key')
    array_item.append(upload_dir)
    condition_array.append(array_item)
    policy_dict['conditions'] = condition_array
    policy = json.dumps(policy_dict).strip()

    policy_encode = base64.b64encode(policy.encode())

    h = hmac.new(accessKeySecret.encode(), policy_encode, sha)
    sign_result = base64.encodebytes(h.digest()).strip()

    callback_dict = {}
    callback_dict['callbackUrl'] = callback_url
    callback_dict['callbackBody'] = 'filename=${object}&size=${size}&mimeType=${mimeType}&height=${imageInfo.height}&width=${imageInfo.width}'
    callback_dict['callbackBodyType'] = 'application/x-www-form-urlencoded'
    callback_param = json.dumps(callback_dict).strip().encode()

    base64_callback_body = base64.b64encode(callback_param)

    token_dict = {}
    token_dict['accessid'] = accessKeyId
    token_dict['host'] = host
    token_dict['policy'] = policy_encode.decode()
    token_dict['signature'] = sign_result.decode()
    token_dict['expire'] = expire_syncpoint
    token_dict['dir'] = upload_dir
    token_dict['callback'] = base64_callback_body.decode()

    return HttpResponse(json.dumps(token_dict))

def osscallback(request):
    pass

def ossimageupload(request):

    # token_dict = get_token()
    # print(token_dict)
    return render(request, 'index.html')


def get_token(request):
    now = int(time.time())
    expire_syncpoint  = now + expire_time
    expire = get_iso_8601(expire_syncpoint)

    policy_dict = {}
    policy_dict['expiration'] = expire
    condition_array = []
    array_item = []
    array_item.append('starts-with')
    array_item.append('$key')
    array_item.append(upload_dir)
    condition_array.append(array_item)
    policy_dict['conditions'] = condition_array
    policy = json.dumps(policy_dict).strip()

    policy_encode = base64.b64encode(policy.encode())

    h = hmac.new(accessKeySecret.encode(), policy_encode, sha)
    sign_result = base64.encodebytes(h.digest()).strip()

    token_dict = {}
    token_dict['accessid'] = accessKeyId
    token_dict['host'] = host
    token_dict['policy'] = policy_encode.decode()
    token_dict['signature'] = sign_result.decode()
    token_dict['expire'] = expire_syncpoint
    token_dict['dir'] = upload_dir

    return HttpResponse(json.dumps(token_dict))