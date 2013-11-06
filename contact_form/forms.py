"""Forms for bitmazk-contact-form application."""
import os

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.utils.translation import ugettext_lazy as _

from .models import ContactFormCategory


def contact_form_category_choices():
    return [(cat.slug, cat.name) for cat in
            ContactFormCategory.objects.all()]


class ContactBaseForm(forms.Form):
    """Base class for contact forms."""
    from_email = settings.DEFAULT_FROM_EMAIL
    recipients = [x[1] for x in settings.CONTACT_FORM_RECIPIENTS]
    subject_template = 'contact_form/contact_form_subject.txt'
    body_template = 'contact_form/contact_form.txt'
    submit_button_value = _('Submit')

    def save(self):
        context = {}
        for info in self.cleaned_data:
            context.update({info: self.cleaned_data.get(info)})
        subject = loader.render_to_string(self.subject_template, context)
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(self.body_template, context)
        send_mail(subject, body, self.from_email, self.recipients,
                  fail_silently=False)
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
        if getattr(settings, 'ENABLE_CAPTCHA', False):
            # Only import captcha app, if captchas are used
            from captcha.fields import CaptchaField
            self.fields['captcha'] = CaptchaField()
        if getattr(settings, 'CONTACT_FORM_DISPLAY_CATEGORIES', False):
            # Only import captcha app, if captchas are used
            self.fields['category'] = forms.ChoiceField(
                choices=contact_form_category_choices(),
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
