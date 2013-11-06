"""URLs for bitmazk-contact-form application."""

from django.conf.urls.defaults import patterns, url

from contact_form.views import ContactFormView


urlpatterns = patterns(
    '',
    url(r'^', ContactFormView.as_view(), name='contact_form'),
)
