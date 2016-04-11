"""Tests for the forms of the `contact_form` app."""
from django.core import mail
from django.test import TestCase

from mixer.backend.django import mixer

from ..forms import AntiSpamContactForm


class AntiSpamContactFormTestCase(TestCase):
    """Test for the ``AntiSpamContactForm`` form class."""
    longMessage = True

    def test_form(self):
        category = mixer.blend('contact_form.ContactFormCategoryTranslation',
                               language_code='en').master
        # The url field is hidden. Only spammers would enter data here.
        # The form should be valid, but send no mail.
        data = {
            'email': 'test@example.com',
            'message': 'Foo',
            'url': 'http://www.example.com',
            'category': category.pk,
        }
        form = AntiSpamContactForm(data=data)
        self.assertFalse(form.errors)
        form.save()
        self.assertEqual(len(mail.outbox), 0)

        # Valid post
        data.update({'url': ''})
        form = AntiSpamContactForm(data=data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(len(mail.outbox), 1)
