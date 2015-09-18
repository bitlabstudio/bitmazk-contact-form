"""Tests for the views of the `contact_form` app."""
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase


class ContactFormViewTestCase(TestCase):
    """Test for the ``ContactFormView`` view."""
    longMessage = True

    def test_view(self):
        resp = self.client.get(reverse('contact_form'))
        self.assertEqual(resp.status_code, 200)
        # The url field is hidden. Only spammers would enter data here.
        # The form should be valid, but send no mail.
        data = {
            'email': 'test@example.com',
            'message': 'Foo',
            'url': 'http://www.example.com',
        }
        resp = self.client.post(reverse('contact_form'), data=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)

        # Valid post
        data.update({'url': ''})
        resp = self.client.post(reverse('contact_form'), data=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
