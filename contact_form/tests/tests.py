"""Unittests for bitmazk-contact-form application."""

from unittest import TestCase
from django.core import mail
from django.test import TestCase as DjangoTestCase
from django.template import RequestContext
from django.test import RequestFactory
from django.contrib.sites.models import RequestSite


from contact_form.tests.utils import (
    get_form_response,
)
from contact_form.forms import ContactForm, ContactBaseForm


class TestSuiteTestCase(TestCase):
    """Test case making sure that test suite setup works properly."""
    def test_test_suite_can_be_run(self):
        self.assertTrue(True)


class IndexViewTestCase(DjangoTestCase):
    """Test case for tests related to IndexView view class."""
    urls = 'contact_form.tests.urls'

    def test_example_view_is_callable(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)

    def test_returns_our_form_object_to_template(self):
        resp = self.client.get('/contact/')
        self.assertTrue(isinstance(resp.context['form'], ContactForm))


class ContactFormTestCase(DjangoTestCase):
    """Test case for ContactForm form class."""
    urls = 'contact_form.tests.urls'

    def test_returns_true_success_on_valid_form_submit(self):
        resp = get_form_response(self.client)
        self.assertTrue(resp.context['success'])

    def test_returns_false_success_on_invalid_email(self):
        resp = get_form_response(self.client, {'email': 'foo@barcom'})
        self.assertFalse(resp.context['success'])

    def test_returns_false_success_on_empty_mandatory_email(self):
        resp = get_form_response(self.client, {'email': ''})
        self.assertFalse(resp.context['success'])

    def test_returns_false_success_on_empty_mandatory_text(self):
        resp = get_form_response(self.client, {'message': ''})
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

    def test_get_context_returns_useful_context(self):
        rf = RequestFactory()
        request = rf.post('/contact/', {
            'name': '',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': ''
        })
        form = ContactBaseForm(data={}, request=request)
        self.assertIsInstance(form.get_context(), RequestContext)

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
        get_form_response(self.client)
        self.assertEqual(len(mail.outbox), 1)

    def test_gets_subject_from_template(self):
        get_form_response(self.client)
        self.assertTrue('Contact form sent' in mail.outbox[0].subject)

    def test_gets_body_from_template(self):
        get_form_response(self.client)
        self.assertTrue('Name:' in mail.outbox[0].body)

    def test_returns_submit_button_value_to_template(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.context['form'].submit_button_value, 'Submit')

    def test_returns_empty_form_after_valid_submit(self):
        resp = get_form_response(self.client)
        self.assertEqual(resp.context['form'].data, {})
