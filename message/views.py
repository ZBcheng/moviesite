import json
import datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import UserProfile

from .models import Message
from .serializers import MessageSerializer

# Create your views here.


class MessageListView(APIView):

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''create a message'''
        request_body = json.loads(request.body, encoding='utf-8')['data']
        message_title = request_body['message_title']  # 信息标题
        message_content = request_body['message_content']  # 信息内容
        sender_name = request_body['sender']  # 获取发件人名
        receiver_list = request_body['receiver']  # 获取收件人名

        # 获取发件人、收件人
        sender = UserProfile.objects.get(username=sender_name)
        send_time = str(datetime.datetime.today())[:10]
        # 创建消息
        message = Message.objects.create(
            message_title=message_title, message_content=message_content, sender=sender,
            send_time=send_time)

        for receiver_name in receiver_list:
            receiver = UserProfile.objects.get(username=receiver_name)
            message.receiver.add(receiver)

        message.save()

        serializer = MessageSerializer(message)
        return Response(serializer.data)


class MessageReceivedView(generics.ListAPIView):
    '''get received messages'''

    serializer_class = MessageSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        message = Message.objects.filter(
            receiver__username__icontains=username)
        return message


class MessageSentView(generics.ListAPIView):
    '''get sent messages'''

    serializer_class = MessageSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        message = Message.objects.filter(sender__username=username)
        return message


class MessageUnreadView(generics.ListAPIView):
    '''get the view of unread messages'''

    serializer_class = MessageSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        message = Message.objects.filter(
            receiver__username__icontains=username).filter(message_status='0')
        return message


class MessageUnreadNum(APIView):
    '''get the num of unread messages'''

    def get(self, request):
        username = request.query_params.get('username')
        message = Message.objects.filter(
            receiver__username__icontains=username).filter(message_status='0').count()
        return Response(message)


class MessageView(APIView):
    '''
    View single messages
    '''

    def get(self, request):
        '''view message'''
        message_id = request.query_params.get('message_id')
        message = Message.objects.get(message_id=message_id)
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def put(self, request):
        '''view and update status'''
        response_body = json.loads(request.body, encoding='utf-8')['data']
        message_id = response_body['message_id']
        message = Message.objects.get(message_id=message_id)
        if message.message_status == '0':
            message.message_status = '1'
            message.save()
        serializer = MessageSerializer(message)
        return Response(serializer.data)
