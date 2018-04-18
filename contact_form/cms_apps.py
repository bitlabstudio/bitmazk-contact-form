"""CMS AppHook for bitmazk-contact-form application."""

from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ContactFormApphook(CMSApp):
    name = _("Contact Form Apphook")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["contact_form.urls"]


apphook_pool.register(ContactFormApphook)
