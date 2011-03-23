from unittest import TestCase
from django.core import mail
from django.test import TestCase as DjangoTestCase
from django.template import RequestContext
from django.contrib.sites.models import Site, RequestSite


from contact_form.tests.utils import RequestFactory
from contact_form.forms import ContactForm, ContactBaseForm


class TestSuiteTestCase(TestCase):
    def test_test_suite_can_be_run(self):
        self.assertTrue(True)


class IndexViewTestCase(DjangoTestCase):
    urls = 'contact_form.tests.urls'

    def test_example_view_is_callable(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)

    def test_returns_our_form_object_to_template(self):
        resp = self.client.get('/contact/')
        self.assertTrue(isinstance(resp.context['form'], ContactForm))


class ContactFormTestCase(DjangoTestCase):
    urls = 'contact_form.tests.urls'

    def test_returns_true_success_on_valid_form_submit(self):
        resp = self.client.post('/contact/', {
            'name': 'tobias',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': 'This is my message.'
            })
        self.assertTrue(resp.context['success'])

    def test_returns_false_success_on_invalid_email(self):
        resp = self.client.post('/contact/', {
            'name': '',
            'email': 'tobias.lorenzbitmazkcom',
            'message': 'This is my message.'
            })
        self.assertFalse(resp.context['success'])

    def test_returns_false_success_on_empty_mandatory_email(self):
        resp = self.client.post('/contact/', {
            'name': '',
            'email': '',
            'message': 'This is my message.'
            })
        self.assertFalse(resp.context['success'])

    def test_returns_false_success_on_empty_mandatory_text(self):
        resp = self.client.post('/contact/', {
            'name': '',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': ''
            })
        self.assertFalse(resp.context['success'])

    def test_get_current_site_returns_current_site(self):
        rf = RequestFactory()
        request = rf.post('/contact/', {
            'name': '',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': ''
            })
        form = ContactForm(data={}, request=request)
        self.assertIsInstance(form.get_current_site(), RequestSite)

    def test_get_context_returns_unseful_context(self):
        rf = RequestFactory()
        request = rf.post('/contact/', {
            'name': '',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': ''
            })
        form = ContactBaseForm(data={}, request=request)
        self.assertIsInstance(form.get_context(), RequestContext)

#Placeholder for template_name() function tests, if you are using such ones

    def test_subject_returns_subject_from_template(self):
        rf = RequestFactory()
        request = rf.post('/contact/', {
            'name': '',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': ''
            })
        form = ContactBaseForm(data={}, request=request)
        self.assertTrue('Contact form sent' in form.subject())

    def test_send_mail_to_dummy_outbox(self):
        resp = self.client.post('/contact/', {
            'name': 'tobias',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': 'This is my message.'
            })
        self.assertEqual(len(mail.outbox), 1)

    def test_gets_subject_from_template(self):
        resp = self.client.post('/contact/', {
            'name': 'tobias',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': 'This is my message.'
            })
        self.assertTrue('Contact form sent' in mail.outbox[0].subject)
