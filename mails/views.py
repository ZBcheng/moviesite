import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import UserProfile
from .models import Mail
from .serializers import MailSerializer
# Create your views here.


class MailListView(APIView):
    '''获取消息列表'''

    def get(self, request):
        messages = Mail.objects.all()
        serialized_messages = MailSerializer(messages, many=True)
        return Response(serialized_messages.data)


class UserMailView(APIView):
    '''用户消息视图📮'''

    def get(self, request):
        '''获取用户发送的消息'''

        params = request.query_params.dict()
        username = params.pop("username")
        user = UserProfile.objects.get(username=username)
        mails = Mail.objects.filter(user=user)
        serialized_mails = MailSerializer(mails, many=True)

        return Response(serialized_mails.data)

    def post(self, request):
        '''新建消息'''

        request_body = json.loads(request.body, encoding='utf-8')['data']
        title = request_body['title']
        content = request_body['content']
        sender_username = request_body['sender_username']
        receiver_username = request_body['receiver_username']
        sender = UserProfile.objects.get(username=sender_username)
        receiver = UserProfile.objects.get(username=receiver_username)
        mail = Mail.objects.create(
            title=title, content=content, sender=sender, receiver=receiver)
        serialized_mail = MailSerializer(mail)

        return Response(serialized_mail.data)
