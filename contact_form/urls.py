"""URLs for bitmazk-contact-form application."""
from django.conf.urls import url

from .views import ContactFormView


urlpatterns = [
    url(r'^', ContactFormView.as_view(), name='contact_form'),
]
