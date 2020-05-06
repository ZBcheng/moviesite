from django.urls import path

from .views import UserView, UserListView, LoginView, RegisterView, StoreUpView, UserStoredView
from .views import UserUpdateView

urlpatterns = [
    path('', UserListView.as_view()),
    path('query', UserView.as_view()),
    path('login', LoginView.as_view()),
    path('update', UserUpdateView.as_view()),
    path('store', StoreUpView.as_view()),
    path('stored', UserStoredView.as_view()),
    path('register', RegisterView.as_view()),
]
