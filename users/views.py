import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from .models import UserProfile
from .serializers import UserProfileSerializer
# Create your views here.


class LoginView(APIView):
    '''
    登录视图
    request.method == 'POST'
    '''

    def post(self, request):
        request_body = json.loads(request.body, encoding='utf-8')['data']
        username = request_body['username']
        print(username)
        password = request_body['password']
        user = authenticate(username=username, password=password)

        print("password correct")
        login(request, user)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        login_user = request.user
        serializer = UserProfileSerializer(login_user)
        return Response({"data": serializer.data, "token": token})


class RegisterView(APIView):
    '''
    用户注册视图
    request.method == 'POST'
    '''

    def post(self, request):
        request_body = json.loads(request.body, encoding='utf-8')
        username = request_body['username']
        phone = request_body['phone']
        email = request_body['email']
        password = request_body['password']
        user = UserProfile.objects.create(
            username=username, phone=phone, email=email, password=make_password(password))
        user.is_superuser = False
        user.save()
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


class UserView(generics.ListAPIView):
    '''
    获取用户信息
    request.method == 'GET'
    '''

    serializer_class = UserProfileSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        user = UserProfile.objects.filter(username=username)
        return user
