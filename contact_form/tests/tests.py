from unittest import TestCase as UnitTestCase
from django.test import TestCase


from contact_form.forms import ContactForm


class TestSuiteTestCase(UnitTestCase):
    def test_test_suite_can_be_run(self):
        self.assertTrue(True)


class IndexViewTestCase(TestCase):
    urls = 'contact_form.tests.urls'

    def test_example_view_is_callable(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)

    def test_returns_our_form_object_to_template(self):
        resp = self.client.get('/contact/')
        self.assertTrue(isinstance(resp.context['form'], ContactForm))

    def test_returns_success_on_valid_form_submit(self):
        resp = self.client.post('/contact/', {
            'name': 'tobias',
            'email': 'tobias.lorenz@bitmazk.com',
            'text': 'This is my message.'
            })
        self.assertTrue(resp.context['success'])


class ContactFormTestCase(TestCase):
    urls = 'contact_form.tests.urls'

    def test_has_mandatory_email_field(self):
        form = ContactForm({})
        self.assertTrue(form.errors.has_key('email'))
