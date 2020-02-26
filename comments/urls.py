from django.urls import path

from .views import CommentListView

urlpatterns = [
    path('', CommentListView.as_view()),
]
