from rest_framework import serializers

from users.serializers import UserProfileSerializer
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    message_status = serializers.CharField(source='get_message_status_display')
    sender = UserProfileSerializer()
    receiver = UserProfileSerializer(many=True)

    class Meta:
        model = Message
        fields = '__all__'

    def get_etype(self, obj):
        '''显示choice value'''
        return obj.get_etype_display()
