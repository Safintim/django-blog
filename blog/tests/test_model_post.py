from datetime import datetime

from blog.models import generation_slug


def test_generation_slug():
    timestamp = int(datetime.now().timestamp())
    text = 'red blue'
    results_generation_slug = generation_slug(text, timestamp=timestamp)
    assert results_generation_slug == f'red-blue-{timestamp}'
