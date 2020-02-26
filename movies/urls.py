from django.urls import path

from .views import MovieView, MovieListView, CategoryListView
from .views import CommentCountView, LikeCountView


urlpatterns = [
    path('', MovieListView.as_view()),
    path('query', MovieView.as_view()),
    path('categories', CategoryListView.as_view()),
    path('likeit', LikeCountView.as_view()),
    path('commentit', CommentCountView.as_view())
]
