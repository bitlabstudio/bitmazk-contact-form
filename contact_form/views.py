"""Views for bitmazk-contact-form application."""
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

from .forms import AntiSpamContactForm, ReCAPTCHAContactForm


class ContactFormView(FormView):
    """View class for the ``contact_form.ContactForm`` Form."""
    template_name = 'contact_form/contact_form.html'

    def get_form_class(self):
        if getattr(settings, 'CONTACT_FORM_RECAPTCHA', False):
            return ReCAPTCHAContactForm
        return AntiSpamContactForm

    def form_valid(self, form):
        form.save()
        success_message = getattr(settings, 'CONTACT_FORM_SUCCESS_MESSAGE', _(
            'Your request has been successfully submitted. We will get back'
            ' to you as soon as possible.'))
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return self.render_to_response(self.get_context_data(
            form=form, contact_form_success=True))
