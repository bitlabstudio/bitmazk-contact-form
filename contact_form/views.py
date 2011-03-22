from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic.list_detail import object_list


from forms import ContactForm

def index(request, template_name='contact_form/contact_form.html'):
    success = False
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            success = True
    else:
        form = ContactForm()
    return render_to_response(template_name,
                              {'success': success, 'form': form})
