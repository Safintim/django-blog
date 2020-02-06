from django.urls import path

from blog.views import PostDetailView, PostListView, TagListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts-list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='posts-detail'),
    path('tags/', TagListView.as_view(), name='tags-list'),
]
