from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from contact_form.forms import ContactForm

urlpatterns = patterns('contact_form.views',
    url(r'^$', view='index', kwargs={'form': ContactForm},
        name='contact_form_index'),
)
