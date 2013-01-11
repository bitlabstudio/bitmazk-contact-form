from django.conf.urls.defaults import *  # NOQA


urlpatterns = patterns(
    '',
    url(r'^contact/', include('contact_form.urls')),
)
