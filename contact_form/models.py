"""Models for the ``contact_form`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from parler.models import TranslatableModel, TranslatedFields


class ContactFormCategory(TranslatableModel):
    """
    The category of the users contact request.

    Is created as translatable master data by the admin.
    For translatable fields check the ``ContactFormCategoryTranslation`` model.

    """
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug'),
    )

    translations = TranslatedFields(
        name=models.CharField(max_length=256),
    )

    def __str__(self):
        return self.safe_translation_getter('name', 'Untranslated')
