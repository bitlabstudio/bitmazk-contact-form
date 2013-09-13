"""Tests for the models of the ``contact_form`` app."""
from django.test import TestCase

from .factories import ContactFormCategoryFactory


class ContactFormCategoryTestCase(TestCase):
    """Tests for the ``ContactFormCategory`` model."""
    longMessage = True

    def test_model(self):
        obj = ContactFormCategoryFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
        self.assertTrue(obj.get_translation(), msg=(
            'The factory should also create a translation'))
