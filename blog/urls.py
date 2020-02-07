from django.urls import path

from blog import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts-list'),
    path('posts/<str:slug>', views.PostDetailView.as_view(), name='posts-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='posts-new'),
    path('about-me/', views.AboutMeView.as_view(), name='about-me')
]
