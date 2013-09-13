"""Models for the ``contact_form`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_libs.models_mixins import SimpleTranslationMixin


class ContactFormCategory(SimpleTranslationMixin, models.Model):
    """
    The category of the users contact request.

    Is created as translatable master data by the admin.
    For translatable fields check the ``ContactFormCategoryTranslation`` model.

    """
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug'),
    )

    def __unicode__(self):
        return self.get_translation().name

    @property
    def name(self):
        return self.get_translation().name


class ContactFormCategoryTranslation(models.Model):
    """Translatable fields of the ``ContactFormCategory`` model."""
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    # needed by simple-translation
    contact_form_category = models.ForeignKey(ContactFormCategory)
    language = models.CharField(max_length=16)

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.language)
