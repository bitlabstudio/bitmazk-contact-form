#!/usr/bin/env python
import os
import sys

from django.conf import settings


if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        ROOT_URLCONF='contact_form.tests.urls',
        CONTACT_FORM_RECIPIENTS=(('Foo Bar', 'foo@example.com'),),
        ENABLE_CAPTCHA=False,
        INSTALLED_APPS=[
            'contact_form',
            'contact_form.tests',
            'captcha',
        ]
    )


from django.test.simple import run_tests


def runtests(*test_args):
    if not test_args:
        test_args = ['tests']
    parent = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "..",
    )
    sys.path.insert(0, parent)
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
