from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView

from blog.filters import PostFilter
from blog.models import Post, Tag


class CommonMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(status='PUB')


class PostListView(CommonMixin, ListView):
    model = Post
    paginate_by = 5
    filter_class = PostFilter

    def get_queryset(self):
        qs = super().get_queryset()
        filtered_posts = self.filter_class(self.request.GET, queryset=qs)
        return filtered_posts.qs


class PostDetailView(CommonMixin, DetailView):
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


class AboutMeView(CommonMixin, TemplateView):
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Post.objects.filter(title='Обо мне', status='PUB').first()
        return context


class ProjectsView(CommonMixin, TemplateView):
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Post.objects.filter(title='Проекты', status='PUB').first()
        return context

