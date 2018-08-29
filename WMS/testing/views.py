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
callback_url = "http://118.126.64.162/testing/osscallback/"

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

# from hashlib import md5
# from M2Crypto import RSA
# from M2Crypto import BIO
from django.http import HttpResponse,JsonResponse
# import urllib3
# from  urllib import parse
# import requests
# from http.server import BaseHTTPRequestHandler

from django.views.decorators.csrf import csrf_exempt,csrf_protect

@csrf_exempt
def osscallback(requests):
    if requests.method == 'POST':
        print("成功访问了！！")
        print("POST数据：")
        print(requests.POST)
        print("\nHEADER为：")
        print(requests.META)
        resp_body = {"Status":"OK","filename":requests.POST.get("filename")}
        return HttpResponse(json.dumps(resp_body),status=200)

        # #get public key
        # pub_key_url = ''
        # post_info = requests.POST
        # try:
        #     pub_key_url_base64 = requests.META.get('x-oss-pub-key-url')
        #     pub_key_url = pub_key_url_base64.decode('base64')
        #     url_reader = post_info('pub_key_url')
        #     pub_key = url_reader.text()
        #     print("获取pub_key")
        # except:
        #     print('pub_key_url : ' + pub_key_url)
        #     print('Get pub key failed!')
        #     # self.send_response(400)
        #     # self.end_headers()
        #     return  HttpResponse(status=400)
        #
        # #get authorization
        # authorization_base64 = requests.META.get('authorization')
        # authorization = authorization_base64.decode('base64')
        #
        # #get callback body
        # content_length = requests.META.get('content-length')
        # callback_body = self.rfile.read(int(content_length))
        #
        # print(self.path)
        #
        # #compose authorization string
        # auth_str = ''
        # pos = self.path.find('?')
        # if -1 == pos:
        #     auth_str = self.path + '\n' + callback_body
        # else:
        #     auth_str = parse.unquote(self.path[0:pos]) + self.path[pos:] + '\n' + callback_body
        #
        # print(auth_str)
        #
        # #verify authorization
        # auth_md5 = md5.new(auth_str).digest()
        # bio = BIO.MemoryBuffer(pub_key)
        # rsa_pub = RSA.load_pub_key_bio(bio)
        #
        # try:
        #     result = rsa_pub.verify(auth_md5, authorization, 'md5')
        # except:
        #     result = False
        #
        # if not result:
        #     print('Authorization verify failed!')
        #     print('Public key : %s' % (pub_key))
        #     print('Auth string : %s' % (auth_str))
        #     self.send_response(400)
        #     self.end_headers()
        #     return
        #
        # #do something accoding to callback_body
        #
        # #response to OSS
        # resp_body = '{"Status":"OK"}'
        # self.send_response(200)
        # self.send_header('Content-Type', 'application/json')
        # self.send_header('Content-Length', str(len(resp_body)))
        # self.end_headers()
        # self.wfile.write(resp_body)

def ossimageupload(request):

    # token_dict = get_token()
    # print(token_dict)
    return render(request, 'ossimageupload.html')


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
