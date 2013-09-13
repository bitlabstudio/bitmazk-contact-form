"""Admins for the ``contact_form`` app."""
from django.contrib import admin
from django.utils.translation import get_language, ugettext_lazy as _

from simple_translation.admin import TranslationAdmin
from simple_translation.utils import get_preferred_translation_from_lang

from .models import ContactFormCategory


class ContactFormCategoryAdmin(TranslationAdmin):
    """Admin for the ``ContactFormCategory`` model."""
    list_display = ['name', 'slug', 'languages', ]

    def name(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).name
    name.short_description = _('Name')


admin.site.register(ContactFormCategory, ContactFormCategoryAdmin)
