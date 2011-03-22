from django.conf.urls.defaults import *


urlpatterns = patterns('contact_form.views',
    url(r'^$', view='index', name='contact_form_index'),
)
