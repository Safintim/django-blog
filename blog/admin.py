from django.contrib import admin

from blog.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'author',
        'created_at',
        'title',
    )

    search_fields = (
        'title',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
    )

    search_fields = (
        'title',
    )
