from rest_framework import serializers

from .models import Movie, MovieCategory


class MovieCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategory
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(many=True)
    directors = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
