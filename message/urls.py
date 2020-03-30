from django.urls import path

from .views import MessageListView, MessageView
from .views import MessageSentView, MessageReceivedView, MessageUnreadView, MessageUnreadNum


urlpatterns = [
    path('', MessageListView.as_view()),
    path('query', MessageView.as_view()),
    path('sent', MessageSentView.as_view()),
    path('recv', MessageReceivedView.as_view()),
    path('unrd', MessageUnreadView.as_view()),
    path('unrd_num', MessageUnreadNum.as_view()),
]
