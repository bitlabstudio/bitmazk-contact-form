from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list


from contact_form.models import Example


def index(request, template_name='contact_form/example_list.html'):
    qs = Example.objects.all()

    try:
        page = int(request.GET.get('page', 0))
    except ValueError:
        raise Http404

    return object_list(
        request,
        queryset=qs,
        template_object_name='example',
	paginate_by=10,
 	page=page,        
    )
