"""URLs for bitmazk-contact-form application."""

from django.conf.urls.defaults import patterns, url

from contact_form.views import ContactFormView


urlpatterns = patterns('contact_form.views',
    url(r'^$', view=ContactFormView.as_view(), name='contact_form'),
)
