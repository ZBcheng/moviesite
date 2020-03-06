from django.urls import path

from .views import MovieView, MovieListView, MovieCategoryListView
from .views import CommentCountView, LikeCountView


urlpatterns = [
    path('', MovieListView.as_view()),
    path('query', MovieView.as_view()),
    path('mvoie_categories', MovieCategoryListView.as_view()),
    path('likeit', LikeCountView.as_view()),
    path('commentit', CommentCountView.as_view())
]
