from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^contact/', include('contact_form.urls')),
)
