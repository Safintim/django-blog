from datetime import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from slugify import slugify

from accounts.models import User
from core.utils import get_filepath


def generation_slug(string: str, timestamp: float = 0) -> str:
    """Generate unique slug by timestamp.

    Args:
        string: example - 'this best post'
        timestamp: for unique slug

    Returns:
        return "this-best-post-1581015344"

    """
    slug = slugify(string, allow_unicode=True)
    current_ts = int(datetime.now().timestamp())
    timestamp = timestamp if timestamp else current_ts
    return f'{slug}-{timestamp}'


class Post(models.Model):
    title = models.CharField('Название', max_length=150, db_index=True)
    description = models.TextField('Описание', null=True, blank=True)
    slug = models.SlugField('Slug', max_length=150, unique=True, blank=True)
    text = models.TextField('Текст')
    image = models.ImageField('Изображение', upload_to=get_filepath, null=True, blank=True)
    STATUS_CHOICE = (
        ('DRAFT', 'Черновик'),
        ('PUB', ' Опубликованно'),
    )
    status = models.CharField('Статус', default='DRAFT', max_length=5, choices=STATUS_CHOICE)
    created_at = models.DateTimeField('Дата создания', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = generation_slug(self.title)
        super().save(*args, **kwargs)

    def get_image_absolute_url(self):
        if self.image:
            return f'{settings.HOST}{self.image.url}'

    def get_absolute_url(self):
        return reverse('posts-detail', kwargs={'slug': self.slug})

    def get_image_html(self):
        if self.image:
            return mark_safe(f'<img src={self.get_image_absolute_url()} width=100>')
        return 'Не загружено'
    get_image_html.short_description = 'Изображение'


class Tag(models.Model):
    title = models.CharField('Название', max_length=150)
    slug = models.CharField('Slug', max_length=150, blank=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = generation_slug(self.title)
        super().save(*args, **kwargs)
