from rest_framework import serializers

from .models import Movie, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(many=True)
    directors = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
