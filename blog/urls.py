from django.urls import path

from blog.views import PostListView, PostDetailView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts-list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='posts-detail'),
]
