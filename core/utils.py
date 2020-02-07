import os

from django.utils.crypto import get_random_string


def get_filepath(instance, filename):
    random_string = get_random_string(15)
    new_filename = f'{random_string}{filename}'
    return os.path.join('static/images', new_filename)
