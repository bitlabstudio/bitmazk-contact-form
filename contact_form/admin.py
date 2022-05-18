"""Admins for the ``contact_form`` app."""
from django.contrib import admin

from parler.admin import TranslatableAdmin

from .models import ContactFormCategory


admin.site.register(ContactFormCategory, TranslatableAdmin)
