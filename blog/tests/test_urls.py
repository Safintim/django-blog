import pytest

from django.urls import reverse


def test_get_list_post(client):
    url = reverse('posts-list')
    response = client.get(url)
    assert response.status_code == 200