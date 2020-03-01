import json

from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import UserProfile
from movies.models import Movie
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.


class CommentListView(APIView):
    '''评论列表视图'''

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class PublisherCommentView(APIView):
    def get(self, request):
        '''获取用户所有评论'''

        params = request.query_params.dict()
        username = params.pop("username")
        user = UserProfile.objects.get(username=username)
        comment = Comment.objects.filter(publisher=user)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''创建新评论'''

        request_body = json.loads(request.body, encoding="utf-8")['data']
        username = request_body['username']
        movie_name = request_body['movie_name']
        content = request_body['content']
        publisher = UserProfile.objects.get(username=username)
        link_movie = Movie.objects.get(name=movie_name)
        comment = Comment.objects.create(
            content=content, publisher=publisher, link_movie=link_movie)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class MovieCommentView(APIView):
    def get(self, request):
        '''获取电影全部评论'''

        params = request.query_params.dict()
        movie_name = params.pop("name")
        comment = Comment.objects.filter(link_movie__name=movie_name)[:1]
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
