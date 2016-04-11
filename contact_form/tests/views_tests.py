"""Tests for the views of the `contact_form` app."""
from django.core import mail
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin
from mixer.backend.django import mixer

from .. import views


class ContactFormViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Test for the ``ContactFormView`` view."""
    view_class = views.ContactFormView

    def test_view(self):
        self.is_callable()
        # The url field is hidden. Only spammers would enter data here.
        # The form should be valid, but send no mail.
        category = mixer.blend('contact_form.ContactFormCategoryTranslation',
                               language_code='en').master
        data = {
            'email': 'test@example.com',
            'message': 'Foo',
            'category': category.pk,
        }
        self.is_postable(data=data, ajax=True)
        self.assertEqual(len(mail.outbox), 1)
