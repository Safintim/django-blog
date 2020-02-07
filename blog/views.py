from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView

from blog.filters import PostFilter
from blog.models import Post, Tag


class PostListView(ListView):
    model = Post
    paginate_by = 5
    filter_class = PostFilter

    def get_queryset(self):
        qs = self.model.objects.all()
        filtered_posts = self.filter_class(self.request.GET, queryset=qs)
        return filtered_posts.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


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


class AboutMeView(TemplateView):
    template_name = 'blog/about_me.html'
