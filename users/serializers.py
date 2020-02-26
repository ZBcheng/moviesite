from rest_framework import serializers

from movies.serializers import MovieSerializer
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    # stored_movies = MovieSerializer

    class Meta:
        model = UserProfile
        fields = ('phone', 'username', 'avatar', 'email')
