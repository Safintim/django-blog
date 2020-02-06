from django.db import models
from django.utils.text import slugify
from datetime import datetime
from accounts.models import User

def generation_slug(string):
    slug = slugify(string, allow_unicode=True)
    timestamp = int(datetime.now().timestamp())
    return f'{slug}-{timestamp}'


class Post(models.Model):
    title = models.CharField('Название', max_length=150, db_index=True)
    slug = models.SlugField('Slug', max_length=150, unique=True, blank=True)
    text = models.TextField('Текст')
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = generation_slug(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField('Название', max_length=150)
    slug = models.CharField('Slug', max_length=150)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.title}'
