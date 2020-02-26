from rest_framework import serializers

from .models import Mail


class MailSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()

    class Meta:
        model = Mail
        fields = '__all__'
