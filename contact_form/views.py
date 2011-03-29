"""Views for bitmazk-contact-form application."""

from django.views.generic import FormView

from forms import ContactForm


class ContactFormView(FormView):
    """View class for the ``contact_form.ContactForm`` Form."""
    form_class = ContactForm
    template_name = 'contact_form/contact_form.html'

    def form_valid(self, form):
        form.save()
        form = self.form_class(request=self.request)
        return self.render_to_response(self.get_context_data(
            form=form, success=True))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(
            form=form, success=False))

    def get_success_url(self):
        pass

    def get_form(self, form_class):
        return form_class(request=self.request, **self.get_form_kwargs())
