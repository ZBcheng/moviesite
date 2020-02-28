from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    stored_movies = serializers.StringRelatedField(many=True)
    saved_categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserProfile
        fields = ('phone', 'username', 'avatar', 'email',
                  'saved_categories', 'stored_movies')
