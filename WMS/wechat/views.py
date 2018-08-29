from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import WechatValidateSerializer


class WechatValidateView(APIView):

    def get(self, request):
        serializer = WechatValidateSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=HTTP_400_BAD_REQUEST
            )

        return HttpResponse(serializer.validated_data["echostr"])

