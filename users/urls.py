from django.urls import path

from .views import UserView, LoginView
from .views import UserUpdateView

urlpatterns = [
    path('', UserView.as_view()),
    path('login', LoginView.as_view()),
    path('update', UserUpdateView.as_view()),
]
