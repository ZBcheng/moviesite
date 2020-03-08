import json

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Movie
from .models import Person, MovieCategory
from .serializers import MovieSerializer
from .serializers import MovieCategorySerializer

# Create your views here.


class AbstractGetter(object):

    def get(self, keywords):
        raise NotImplementedError


class MovieCategoryGetter(AbstractGetter):
    '''get movie by the type'''

    def get(self, keywords):
        '''
        Args:
            key: type of the movie
        '''
        movies = Movie.objects.filter(
            category__name__icontains=keywords)
        return movies


class NameGetter(AbstractGetter):
    '''get movie by the name of the movie'''

    def get(self, keywords):
        '''
        Args:
            keywords: name of the movie
        '''
        movies = Movie.objects.get(name=keywords)
        return movies


class DirectorNameGetter(AbstractGetter):
    '''get movie by directors' name'''

    def get(self, keywords):
        '''
        Args:
            keywords: name of the director
        '''
        # director = Person.objects.get(name=keywords)
        movies = Movie.objects.filter(directors__name__icontains=keywords)
        return movies


class ActorNameGetter(AbstractGetter):
    '''get movie by actors' name'''

    def get(self, keywords):
        '''
        Args:
            keywords: name of the actor
        '''
        # actor = Person.objects.get(name=keywords)
        movies = Movie.objects.filter(actors__name__icontains=keywords)
        return movies


class MovieGetter(object):
    def __init__(self, getter, keywords):
        '''
        Args:
            getter: isinstance(getter, AbstractGetter) == True
            keywords: the keyword you will use to search movies
        '''
        self.getter = getter  # getter类型
        self.keywords = keywords  # 搜索关键字

    def get(self):
        '''
        Returns: QuerySet of the search result of the keywords
        '''
        return self.getter.get(self.keywords)


class MovieView(generics.ListAPIView):
    '''根据关键字获取电影列表'''

    serializer_class = MovieSerializer

    def get_queryset(self):
        params = self.request.query_params.dict()
        try:
            name = params.pop('name')
        except KeyError:
            name = None

        try:
            director_name = params.pop('director_name')
        except KeyError:
            director_name = None

        try:
            actor_name = params.pop('actor_name')
        except KeyError:
            actor_name = None

        try:
            category = params.pop('category')
        except KeyError:
            category = None

        if name:
            getter = MovieGetter(NameGetter(), name)
        elif director_name:
            getter = MovieGetter(DirectorNameGetter(), director_name)
        elif actor_name:
            getter = MovieGetter(ActorNameGetter(), actor_name)
        elif category:
            getter = MovieGetter(MovieCategoryGetter(), category)
        return getter.get()


class MovieListView(CacheResponseMixin, generics.ListAPIView):
    '''获取电影列表'''

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieCategoryListView(CacheResponseMixin, APIView):
    '''获取电影类型列表'''

    def get(self, request):
        categories = MovieCategory.objects.all()
        serializer = MovieCategorySerializer(categories, many=True)
        return Response(serializer.data)


class LikeCountView(APIView):
    '''点赞或取消赞'''

    def post(self, request):
        request_body = json.loads(request.body)['data']
        movie_id = request_body['id']
        cal = request_body['cal']
        movie = Movie.objects.get(id=movie_id)
        if cal == 'add':
            movie.like_count += 1
        elif cal == 'dec':
            movie.like_count -= 1
        else:
            raise Exception('undefined cal')
        movie.save()
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class CommentCountView(APIView):
    '''添加评论'''

    def post(self, request):
        request_body = json.loads(request.body)['data']
        movie_id = request_body['id']
        movie = Movie.objects.get(id=movie_id)
        movie.comment_count += 1
        movie.save()
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
