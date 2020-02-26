from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    stored_movies = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'phone', 'stored_movies')
