"""Factories for the models of the ``contact_form`` app."""
import factory
from django_libs.tests.factories import SimpleTranslationMixin

from ..models import ContactFormCategory, ContactFormCategoryTranslation


class ContactFormCategoryBaseFactory(factory.Factory):
    """The basic Factory for a ``ContactFormCategory`` without translation."""
    FACTORY_FOR = ContactFormCategory

    slug = factory.Sequence(lambda n: 'slug_{0}'.format(n))


class ContactFormCategoryFactory(SimpleTranslationMixin, factory.Factory):
    """Factory for ``ContactFormCategory`` objects."""

    @staticmethod
    def _get_translation_factory_and_field():
        return (ContactFormCategoryTranslationFactory, 'contact_form_category')


class ContactFormCategoryTranslationFactory(factory.Factory):
    """Factory for ``ContactFormCategoryTranslation`` objects."""
    FACTORY_FOR = ContactFormCategoryTranslation

    name = factory.Sequence(lambda n: 'category name {0}'.format(n))
    contact_form_category = factory.SubFactory(ContactFormCategoryBaseFactory)
    language = 'en'
