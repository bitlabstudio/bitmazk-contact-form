bitmazk-contact-form
====================

A reusable contact form app for Django. Ready for multilingual sites.

At the moment this contact form does not redirect to a success page. Instead
it adds a variable ``success`` to the template context. The developer can then
just output some success message next to the form.

The project aims to be used in conjunction with `django-cms
<https://github.com/divio/django-cms>`_. Therefore the package comes with a
``cms_app.py`` file and can be integrated into your CMS pages via an AppHook.
We might add a ``cms_plugins.py``, as well.

The code is heavily influenced by the wonderful `django-contact-form
<https://github.com/jezdez/django-contact-form>`_ of `Jannis Leidel
<https://github.com/jezdez>`_. We just applied our own coding standards and
ported it to Class Based Generic Views. In fact, this project has lesser
features than the original one (i.e. no spam protection, yet)!

Prerequisites
=============

- Django 1.3

Installation
============

* Install this package::

    pip install -e git://github.com/bitmazk/bitmazk-contact-form#egg=contact_form

* Add ``contact_form`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        [...]
        'contact_form',
    }

* Add ``CONTACT_FORM_RECEPIENTS`` to your ``settings.py``::

    CONTACT_FORM_RECEPIENTS = (
        ('Foo Bar', 'foobar@example.com'),
    )

* Make sure to have a block called ``contact_form`` in your template::

  {% block contact_form %}

* If the output does not fit your needs, just override the templates provided
  by this package.

* Create a CMS page, assign it the template that has the ``contact_form`` block
  and add the ``Contact Form AppHook`` to the page.

Configuration
=============

Set ``ENABLE_CAPTCHA=True`` if you want to show an image captcha.

TODO: Describe email settings for settings.py
