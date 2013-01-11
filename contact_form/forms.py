"""Forms for bitmazk-contact-form application."""
from django import forms
from django.conf import settings
from django.contrib.sites.models import Site, RequestSite
from django.core.mail import send_mail
from django.template import loader, RequestContext
from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField


class ContactBaseForm(forms.Form):
    """Base class for contact forms."""
    def __init__(self, data=None, files=None, request=None, *args, **kwargs):
        if request is None:
            raise TypeError(_('Keyword argument "request" must be supplied'))
        super(ContactBaseForm, self).__init__(data=data, files=files, *args,
                                              **kwargs)
        self.request = request

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [
            mail_tuple[1] for mail_tuple in settings.CONTACT_FORM_RECIPIENTS]
    subject_template_name = 'contact_form/contact_form_subject.txt'
    template_name = 'contact_form/contact_form.txt'
    submit_button_value = _('Submit')

    def message(self):
        """Returns the email message based on the email template."""
        if callable(self.template_name):
            template_name = self.template_name()
        else:
            template_name = self.template_name
        return loader.render_to_string(template_name,
                                       self.get_context())

    def subject(self):
        """Returns the email subject based on the subject template."""
        if callable(self.template_name):
            template_name = self.subject_template_name()
        else:
            template_name = self.subject_template_name
        subject = loader.render_to_string(template_name,
                                          self.get_context())
        return ''.join(subject.splitlines())

    def get_context(self):
        """Returns a RequestContext, adds cleaned_data and the current Site to the context."""
        if not self.is_valid():
            raise ValueError(
                _('Cannot generate Context from invalid contact form'))
        return RequestContext(self.request,
                              dict(self.cleaned_data,
                                   site=self.get_current_site()))

    def get_message_dict(self):
        """Returns a message dict. Should be consumed by ``django.core.mail.send_mail()``."""
        if not self.is_valid():
            raise ValueError(
                _('Message cannot be sent from invalid contact form'))
        message_dict = {}
        for message_part in ('from_email', 'message', 'recipient_list',
                             'subject'):
            attr = getattr(self, message_part)
            message_dict[message_part] = callable(attr) and attr() or attr
        return message_dict

    def get_current_site(self):
        """Checks if the sites app is installed and returns a ``RequestSite`` instance if not."""
        if Site._meta.installed:
            return Site.objects.get_current()
        return RequestSite(self.request)

    def save(self, fail_silently=False):
        send_mail(fail_silently=fail_silently, **self.get_message_dict())


class ContactForm(ContactBaseForm):
    """A typical contact form."""

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if settings.ENABLE_CAPTCHA:
            self.fields['captcha'] = CaptchaField()

    name = forms.CharField(
        label=_('Name'), max_length=255, required=False)
    email = forms.EmailField(
        label=_('Email'), required=True)
    message = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs=dict(maxlength=5000)),
        label=_('Message'),
        required=True)
