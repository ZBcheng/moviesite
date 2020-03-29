import os
import json
import base64

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from moviesite.settings import MEDIA_URL
from .models import UserProfile
from .serializers import UserProfileSerializer
# Create your views here.


class LoginView(APIView):
    '''user login'''

    def post(self, request):

        request_body = json.loads(request.body, encoding='utf-8')['data']
        username = request_body['username']
        password = request_body['password']
        # user = authenticate(username=username, password=password)

        print(username)
        print(password)

        try:
            user = authenticate(username=username, password=password)
        except UserProfile.DoesNotExist:
            print("user does not exist")
            return Response("user does not exist")
        # except users.models.UserProfile.DoesNotExist as e:
            # raise(e)

        # if user.password != make_password(password):
        #     print("wrong password")
        #     return Response("wrong password")

        user.backend = 'django.contrib.auth.backends.ModelBackend'
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


class UserUpdateView(APIView):
    '''update the view of a specific user'''

    def put(self, request):
        request_body = json.loads(request.body, encoding='utf-8')['data']
        username = request_body['username']
        user = UserProfile.objects.get(username=username)

        # optional keys
        try:
            phone = request_body['phone']
        except KeyError:
            phone = user.phone
        try:
            email = request_body['email']
        except KeyError:
            email = user.email

        avatar_name = request_body['avatar_name']  # the name of the image
        avatar_url = request_body['avatar_url']  # the url of the image

        if avatar_url.startswith('http'):
            # that means user didn't change his/her avatar
            pass
        else:
            # in this situation, avatar_url is a str object encoded with base64
            real_url = get_real_url(avatar_url)
            save_as_img(avatar_name, real_url)
            user.avatar = 'avatar/' + avatar_name  # save path

        user.phone = phone
        user.email = email
        user.save()
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


def get_real_url(raw_url: str) -> str:
    '''
    remove trush data in raw_url
    Args:
        raw_url: raw url get from frontend
    '''

    return raw_url.split(',')[1]


def save_as_img(img_name: str, b64_url: str):
    '''
    convert image url to jpg
    Args:
        img_name: the name of the jpg file
        b64_url: a str object encoded with base64
    '''

    bin_url = base64.b64decode(b64_url)
    current_path = os.path.abspath(__file__)
    project_path = os.path.abspath(
        os.path.dirname(current_path) + os.path.sep + "..")  # the path of the django project
    file_path = project_path + MEDIA_URL + 'avatar/' + img_name

    with open(file_path, 'wb') as file:
        file.write(bin_url)

    return True
