import django_filters

from django.db.models import Q

from blog.models import Post


class PostFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(lookup_expr='title', field_name='tags')
    search = django_filters.CharFilter(method='search_by_title_and_text')

    class Meta:
        model = Post
        fields = {
            'text': ['icontains', ]
        }

    def search_by_title_and_text(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(text__icontains=value))
