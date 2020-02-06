from django.urls import path

from blog.views import PostListView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts-list')
]
