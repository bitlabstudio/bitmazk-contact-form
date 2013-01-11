"""Tests for the forms of the `contact_form` app."""
from django.conf import settings
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
        self.assertEqual(mail.outbox[0].subject,
                         'Contact form sent by test@example.com')
        self.assertEqual(mail.outbox[0].body,
                         'Name: \nEmail: test@example.com\n\nMessage: Foo')

        # Enable CAPTCHA
        settings.ENABLE_CAPTCHA = True
        form = AntiSpamContactForm(data=data)
        self.assertFalse(form.is_valid())
