from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()
    link_movie = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'
