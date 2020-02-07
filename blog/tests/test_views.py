import pytest
from django.urls import reverse
from mixer.backend.django import mixer

from blog.models import Post
from blog.tests.common_fixtures import auto_login_user, create_user, test_password


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


@pytest.mark.django_db
def test_redirect_after_create_post(auto_login_user):
    client, user = auto_login_user()
    data = {
        'title': 'The best post about django',
        'text': 'More text',
    }
    url = reverse('posts-new')
    response = client.post(url, data=data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_post(auto_login_user):
    client, user = auto_login_user()
    data = {
        'title': 'The best post about django',
        'text': 'More text',
    }
    url = reverse('posts-new')
    client.post(url, data=data)

    post = Post.objects.get(pk=1)
    assert post.author == user
    assert post.title == data['title']


def test_get_list_tags(client):
    url = reverse('tags-list')
    response = client.get(url)
    assert response.status_code == 200
