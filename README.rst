bitmazk-contact-form
====================

A reusable contact form app for Django. Can be used with a modern user-friendly
spam protection. Ready for multilingual sites.

At the moment this contact form does not redirect to a success page. Instead
it adds a variable ``success`` to the template context. The developer can then
just output some success message next to the form.

The project can be used in conjunction with `django-cms
<https://github.com/divio/django-cms>`_. Therefore the package comes with a
``cms_app.py`` file and can be integrated into your CMS pages via an AppHook.

The code is heavily influenced by the wonderful `django-contact-form
<https://github.com/jezdez/django-contact-form>`_ of `Jannis Leidel
<https://github.com/jezdez>`_. We just applied our own coding standards and
ported it to Class Based Generic Views.

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

Add the relevant css sheet::

    <link href="{% static "contact_form/css/contact_form.css" %}" type="text/css" media="all" rel="stylesheet" />

optional::

* Create a CMS page, assign it to the template that has the ``contact_form``
block and add the ``Contact Form AppHook`` to the page.


Configuration
=============

Set ``CONTACT_FORM_DISPLAY_CATEGORIES=True`` if you want the form to include a
list of categories the users request is about.

The categories are stored as master data and you can add them via the Django
admin under ``contact_form > ContactFormCategory``.
