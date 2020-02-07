from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from blog.models import Post, Tag


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = (
        'title',
        'text',
    )

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)


class TagListView(ListView):
    model = Tag
