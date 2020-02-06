from django.views.generic import DetailView, ListView

from blog.models import Post, Tag


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class TagListView(ListView):
    model = Tag
