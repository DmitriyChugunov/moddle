from django.contrib import admin
from django.urls import path, include

from .views import PostView, PostIdView

urlpatterns = [
    path('', PostView),
    path('/post/<int:id>', PostIdView, name='post')
]