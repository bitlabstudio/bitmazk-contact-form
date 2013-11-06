"""Views for bitmazk-contact-form application."""
from django.views.generic import FormView

from contact_form.forms import AntiSpamContactForm


class ContactFormView(FormView):
    """View class for the ``contact_form.ContactForm`` Form."""
    form_class = AntiSpamContactForm
    template_name = 'contact_form/contact_form.html'

    def form_valid(self, form):
        form.save()
        return self.render_to_response(self.get_context_data(form=form,
                                                             success=True))
