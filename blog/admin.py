from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blog.models import Post, Tag


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display_links = (
        'id',
        'created_at',
        'title',
        'get_image_html',
    )

    list_display = (
        'id',
        'created_at',
        'status',
        'title',
        'get_image_html',
    )

    fieldsets = (
        (None, {
            'fields': (('title', 'slug'),)
        }),
        (None, {
            'fields': (('image', 'get_image_html'),)
        }),
        (None, {
            'fields': (('description', 'text', ),)
        }),
        ('Автор И теги', {
            'classes': ('collapse', ),
            'fields': (('created_at', 'author', 'tags', 'status'),)
        }),
    )

    readonly_fields = ('created_at', 'get_image_html', )

    search_fields = (
        'author__email',
        'title',
        'text',
        'slug'
    )

    list_filter = ('tags', 'status', )

    list_editable = ('status', )
    save_on_top = True


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
    )

    search_fields = (
        'title',
        'slug',
    )
