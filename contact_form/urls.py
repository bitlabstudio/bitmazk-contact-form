from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('contact_form.views',
    url(r'^$', view='index', name='contact_form_index'),
)
