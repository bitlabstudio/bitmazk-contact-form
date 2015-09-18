"""Tests for the forms of the `contact_form` app."""
from django.core import mail
from django.test import TestCase

from contact_form.forms import AntiSpamContactForm


class AntiSpamContactFormTestCase(TestCase):
    """Test for the ``AntiSpamContactForm`` form class."""
    longMessage = True

    def test_form(self):
        # The url field is hidden. Only spammers would enter data here.
        # The form should be valid, but send no mail.
        data = {
            'email': 'test@example.com',
            'message': 'Foo',
            'url': 'http://www.example.com',
        }
        form = AntiSpamContactForm(data=data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(len(mail.outbox), 0)

        # Valid post
        data.update({'url': ''})
        form = AntiSpamContactForm(data=data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(len(mail.outbox), 1)
