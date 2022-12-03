from django.urls import path
from ohstagram.views import Login, Join

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('join', Join.as_view(), name='join'),
]