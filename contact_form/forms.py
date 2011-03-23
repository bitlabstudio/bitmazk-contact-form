from django import forms

from django.conf import settings
from django.core.mail import send_mail


class ContactBaseForm(forms.Form):
    def save(self, fail_silently=False):
        message_dict = {
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'message': (self.cleaned_data['message']),
            'recipient_list': [
                mail_tuple[1] for mail_tuple in settings.MANAGERS],
            'subject': ('Contact form submitted by %s (%s)'
                        % (self.cleaned_data['name'],
                           self.cleaned_data['email'],))
        }
        send_mail('Subject here', 'Here is the message.', 'from@example.com',
    ['to@example.com'], fail_silently=False)

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
