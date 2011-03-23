from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.views.generic.list_detail import object_list


from forms import ContactForm, AkismetContactForm

def index(request,
          template_name='contact_form/contact_form.html',
          form=ContactForm,
          fail_silently=False):
    success = False
    if request.POST:
        form = form(data=request.POST, files=request.FILES, request=request)
        if form.is_valid():
            success = True
            form.save(fail_silently=False)
    else:
        form = form(request=request)
    return render_to_response(template_name,
                              {'success': success, 'form': form})
