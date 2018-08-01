from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import WechatValidateSerializer


class WechatValidate(APIView):

    def get(self, request):
        # return HttpResponse("test")

        serializer = WechatValidateSerializer(data=request.QUERY_PARAMS)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return HttpResponse(serializer.validated_data("echostr"))
