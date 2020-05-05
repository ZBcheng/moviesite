from django.urls import path

from .views import MovieView, MovieListView, MovieCategoryListView, SingleView
from .views import CompilationView, CompilationListView
from .views import CommentCountView, LikeCountView


urlpatterns = [
    path('', MovieListView.as_view()),
    path('query', MovieView.as_view()),
    path('comp', CompilationListView.as_view()),
    path('comp/query', CompilationView.as_view()),
    path('view', SingleView.as_view()),
    path('mv_categories', MovieCategoryListView.as_view()),
    path('likeit', LikeCountView.as_view()),
    path('commentit', CommentCountView.as_view())
]
