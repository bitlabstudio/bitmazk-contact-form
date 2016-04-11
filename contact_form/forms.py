"""Forms for bitmazk-contact-form application."""
import os

from django import forms
from django.conf import settings
from django.utils.translation import get_language, ugettext_lazy as _

from django_libs.utils_email import send_email

from .models import ContactFormCategory


class ContactBaseForm(forms.Form):
    """Base class for contact forms."""
    from_email = settings.DEFAULT_FROM_EMAIL
    recipients = [x[1] for x in settings.CONTACT_FORM_RECIPIENTS]
    subject_template = 'contact_form/email/contact_form_subject.html'
    body_template = 'contact_form/email/contact_form.html'
    submit_button_value = _('Submit')

    def save(self):
        context = {}
        for info in self.cleaned_data:
            context.update({info: self.cleaned_data.get(info)})
        send_email(
            None,
            context,
            self.subject_template,
            self.body_template,
            self.from_email,
            self.recipients,
            priority="medium",
            reply_to=self.cleaned_data.get('email', ''),
        )
        # Empties the form
        self.data = {}


class ContactForm(ContactBaseForm):
    """A typical contact form."""
    name = forms.CharField(
        label=_('Name'),
        max_length=255,
        required=False,
    )

    email = forms.EmailField(
        label=_('Email'),
    )

    message = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs=dict(maxlength=5000)),
        label=_('Message'),
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if getattr(settings, 'CONTACT_FORM_DISPLAY_CATEGORIES', False):
            self.fields['category'] = forms.ModelChoiceField(
                queryset=ContactFormCategory.objects.language(get_language()),
                label=_('Category'),
                help_text=_('Please tell us the subject of your request.'),
            )


class AntiSpamContactForm(ContactForm):
    """A modern contact form, which works without captchas."""
    url = forms.URLField(required=False)

    class Media:
        css = {
            'all': (os.path.join(
                settings.STATIC_URL, 'contact_form/css/contact_form.css'), )
        }
        js = (
            os.path.join(
                settings.STATIC_URL, 'contact_form/js/contact_form.js', ),
        )

    def save(self):
        if not self.cleaned_data.get('url'):
            return super(AntiSpamContactForm, self).save()
