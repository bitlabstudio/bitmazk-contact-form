bitmazk-contact-form
====================

A reusable contact form app for Django. Can be used with a modern user-friendly
spam protection or Google's reCAPTCHA. Ready for multilingual sites.

At the moment this contact form does not redirect to a success page. Instead
it adds a variable ``contact_form_success`` to the template context. The
developer can then just output some success message next to the form.

The project can be used in conjunction with `django-cms
<https://github.com/divio/django-cms>`_. Therefore the package comes with a
``cms_app.py`` file and can be integrated into your CMS pages via an AppHook.

Prerequisites
=============

- see requirements.txt

Installation
============

If you want to install the latest stable release from PyPi:

    $ pip install bitmazk-contact-form

If you feel adventurous and want to install the latest commit from GitHub:

    $ pip install -e git://github.com/bitmazk/bitmazk-contact-form#egg=contact_form

Add ``contact_form`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        [...]
        'contact_form',
    }

Add ``CONTACT_FORM_RECIPIENTS`` to your ``settings.py``::

    CONTACT_FORM_RECIPIENTS = (
        ('Foo Bar', 'foobar@example.com'),
    )

Make sure to have a block called ``contact_form`` in your template::

  {% block contact_form %}

If the output does not fit your needs, just override the templates provided by
this package.

With Django-CMS
---------------

Create a CMS page, assign it to the template that has the ``contact_form``
block and add the ``Contact Form AppHook`` to the page.

Simple spam protection
----------------------

Make sure you got a content block named ``extracss`` or add the relevant css sheet::

    {{ form.media.css }}

reCAPTCHA
---------

First register at https://www.google.com/recaptcha/ and make sure you added all
the relevant URLs to your captcha.

Install ``django-recaptcha``:

    pip install django-recaptcha

Add it to your installed apps.

Now add the following settings::

    CONTACT_FORM_RECAPTCHA = True
    RECAPTCHA_PUBLIC_KEY = 'YOUR_GOOGLE_RECAPTCHA_PUBLIC_KEY'
    RECAPTCHA_PRIVATE_KEY = 'YOUR_GOOGLE_RECAPTCHA_PRIVATE_KEY'
    NOCAPTCHA = True
    RECAPTCHA_USE_SSL = True  # We assume you are using https://

Configuration
=============

Set ``CONTACT_FORM_DISPLAY_CATEGORIES=True`` if you want the form to include a
list of categories the users request is about.

The categories are stored as master data and you can add them via the Django
admin under ``contact_form > ContactFormCategory``.
