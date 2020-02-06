import pytest
from django.urls import reverse
from mixer.backend.django import mixer

from blog.models import Post


def test_get_list_post(client):
    url = reverse('posts-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_detail_post(client):
    post = mixer.blend(Post)
    url = reverse('posts-detail', kwargs={'pk': post.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_get_list_tags(client):
    url = reverse('tags-list')
    response = client.get(url)
    assert response.status_code == 200
