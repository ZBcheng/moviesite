from django.urls import path

from .views import UserView, LoginView, RegisterView
from .views import UserUpdateView

urlpatterns = [
    path('', UserView.as_view()),
    path('login', LoginView.as_view()),
    path('update', UserUpdateView.as_view()),
    path('register', RegisterView.as_view())
]
