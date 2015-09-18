"""Tests for the models of the ``contact_form`` app."""
from django.test import TestCase

from mixer.backend.django import mixer


class ContactFormCategoryTestCase(TestCase):
    """Tests for the ``ContactFormCategory`` model."""
    longMessage = True

    def test_model(self):
        obj = mixer.blend('contact_form.ContactFormCategory')
        self.assertTrue(str(obj), msg=(
            'Should be able to instantiate and save the model.'))
