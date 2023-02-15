from rest_framework.views import APIView
from rest_framework.response import Response

import requests
import json

from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# 获取用户数据
class UserData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print('Get data: ', request.user.profile.items)
        return Response({'code': 'get ok', 'items': request.user.profile.items['items']})

    def post(self, request, format=None):
        user = request.user
        user.profile.items = request.data
        user.save()
        print('Post data: ', user.profile.items)
        return Response({'code': 'post ok'})

# 微信登录
class WeixinLogin(APIView):
    def post(self, request, format=None):
        print('Post data: ', request.data)
        """
        提供 post 请求
        """
        # 从请求中获得code
        code = request.data['code']
        print(code)
        # 填写你的测试号密钥
        appid = 'wx6bd62a30b5e36cae'
        appsecret = 'b05fca3ef020639b5acfae61b2678310'
        # 微信服务接口地址
        base_url = 'https://api.weixin.qq.com/sns/jscode2session'
        # 实际请求
        url = base_url + "?appid=" + appid + "&secret=" + appsecret + "&js_code=" + code + "&grant_type=authorization_code"
        print(url)
        response = requests.get(url, verify=False)
        print(response.json())
        # 处理获取的 openid 
        try:
            openid = response.json()['openid']
            session_key = response.json()['session_key']
        except KeyError:
            return Response({'code': 'fail'})
        else:
            # 打印到后端命令行
            print(openid, session_key)

            try:
                user = User.objects.get(username=openid)
            except User.DoesNotExist:
                user = None

            if user:
                user = User.objects.get(username=openid)
            else:
                user = User.objects.create(
                    username=openid,
                    password=openid
                )

            return Response({
                    'code': 'success',
                    'access': openid,
                })