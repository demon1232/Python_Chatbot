from django.urls import path
from .views import chat_view, home

urlpatterns = [
    path('', home),
    path('chat/', chat_view),
]