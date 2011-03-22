from unittest import TestCase as UnitTestCase
from django.core import mail
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


class ContactFormTestCase(TestCase):
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

    def test_send_mail_to_dummy_outbox(self):
        resp = self.client.post('/contact/', {
            'name': 'tobias',
            'email': 'tobias.lorenz@bitmazk.com',
            'message': 'This is my message.'
            })
        self.assertEqual(mail.outbox[0].from_email, 'from@example.com')