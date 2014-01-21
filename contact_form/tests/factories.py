"""Factories for the models of the ``contact_form`` app."""
import factory
from django_libs.tests.factories import HvadFactoryMixin

from ..models import ContactFormCategory


class ContactFormCategoryFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """The Factory for a ``ContactFormCategory``."""
    FACTORY_FOR = ContactFormCategory

    language_code = 'en'
    name = factory.Sequence(lambda x: 'Category {}'.format(x))
