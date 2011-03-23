from django import forms

from django.conf import settings
from django.core.mail import send_mail
from django.template import loader, RequestContext
from django.contrib.sites.models import Site, RequestSite


class ContactBaseForm(forms.Form):
    def __init__(self, data=None, files=None, request=None, *args, **kwargs):
        if request is None:
            raise TypeError("Keyword argument 'request' must be supplied")
        super(ContactBaseForm, self).__init__(data=data, files=files, *args,
                                              **kwargs)
        self.request = request

    from_email = settings.DEFAULT_FROM_EMAIL

    recipient_list = [mail_tuple[1] for mail_tuple in settings.MANAGERS]

    subject_template_name = 'contact_form/contact_form_subject.txt'

    template_name = 'contact_form/contact_form.txt'

    def message(self):
        if callable(self.template_name):
            template_name = self.template_name()
        else:
            template_name = self.template_name
        return loader.render_to_string(template_name,
                                       self.get_context())

    def subject(self):
        if callable(self.template_name):
            template_name = self.template_name()
        else:
            template_name = self.template_name
        subject = loader.render_to_string(self.subject_template_name,
                                          self.get_context())
        return ''.join(subject.splitlines())

    def get_context(self):
        if not self.is_valid():
            raise ValueError("Cannot generate Context from invalid contact form")
        return RequestContext(self.request,
                              dict(self.cleaned_data,
                                   site=self.get_current_site()))

    def get_message_dict(self):
        if not self.is_valid():
            raise ValueError("Message cannot be sent from invalid contact form")
        message_dict = {}
        for message_part in ('from_email', 'message', 'recipient_list',
                             'subject'):
            attr = getattr(self, message_part)
            message_dict[message_part] = callable(attr) and attr() or attr
        return message_dict

    def get_current_site(self):
        if Site._meta.installed:
            return Site.objects.get_current()
        return RequestSite(self.request)

    def save(self, fail_silently=False):
        send_mail(fail_silently=fail_silently, **self.get_message_dict())


class ContactForm(ContactBaseForm):
    name = forms.CharField(
        label='c_name', max_length=255, required=False, initial='Your Name.')
    email = forms.EmailField(
        label='c_mail', initial='Your Email.', required=True)
    message = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs=dict(maxlength=5000)),
        label='c_text',
        required=True,
        initial='Your Message.')

class AkismetContactForm(ContactForm):
    def clean_message(self):
        if 'message' in self.cleaned_data and getattr(settings,
                                                      'AKISMET_API_KEY', ''):
            from akismet import Akismet
            from django.utils.encoding import smart_str
            akismet_api = Akismet(key=settings.AKISMET_API_KEY,
                                  blog_url='http://%s/' %
                                  self.get_current_site().domain)
            if akismet_api.verify_key():
                akismet_data = { 'comment_type': 'comment',
                                 'referer': self.request.META.get(
                                     'HTTP_REFERER', ''),
                                 'user_ip': self.request.META.get(
                                     'REMOTE_ADDR', ''),
                                 'user_agent': self.request.META.get(
                                     'HTTP_USER_AGENT', '') }
                if akismet_api.comment_check(
                    smart_str(self.cleaned_data['body']),
                    data=akismet_data, build_data=True):
                    raise forms.ValidationError(
                        _("Akismet thinks this message is spam"))
        return self.cleaned_data['message']
