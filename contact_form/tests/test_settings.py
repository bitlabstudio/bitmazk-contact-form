"""Settings that need to be set in order to run the tests."""
import os

DEBUG = True
SITE_ID = 1

CONTACT_FORM_RECIPIENTS = (
    ('Test', 'test@example.com'),
)
ENABLE_CAPTCHA = False

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

CURRENT_DIR = os.path.dirname(__file__)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = 'contact_form.tests.urls'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(CURRENT_DIR, '../../static/')

STATICFILES_DIRS = (
    os.path.join(CURRENT_DIR, 'test_static'),
)

TEMPLATE_DIRS = (
    os.path.join(CURRENT_DIR, './templates'),
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    CURRENT_DIR, 'coverage')

COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'test_app$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]

INTERNAL_APPS = [
    'contact_form',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS
