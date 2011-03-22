from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='c_name', max_length=255, required=False, initial='Your Name.')
    email = forms.EmailField(
        label='c_mail', initial='Your Email.', required=True)
    text = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs=dict(maxlength=5000)),
        label='c_text',
        required=True,
        initial='Your Message.')