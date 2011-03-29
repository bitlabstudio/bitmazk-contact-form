from django.test import Client
from django.core.handlers.wsgi import WSGIRequest


def get_form_response(client, overrides={}):
    """Returns the response to a valid POST request."""
    defaults = {
        'name': 'Name',
        'email': 'foobar@example.com',
        'message': 'Foo bar.',
    }
    defaults.update(overrides)
    return client.post('/contact/', data=defaults)
