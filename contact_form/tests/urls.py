from django.conf.urls.defaults import *  # NOQA


urlpatterns = patterns(
    '',
    url(r'^', include('contact_form.urls')),
)
