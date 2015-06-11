# python setup.py test
#   or
# python runtests.py

import sys

from django import VERSION as django_version
from django.conf import settings

APP = 'countries_plus'
TEST_APP = APP + '.tests'
ADMIN = 'django.contrib.admin'
if django_version >= (1, 7):
    ADMIN = 'django.contrib.admin.apps.SimpleAdminConfig'

settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    ROOT_URLCONF=TEST_APP + '.urls',
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        ADMIN,
        APP,
        TEST_APP,
    ),
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'countries_plus.middleware.AddRequestCountryMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    ),
    TEMPLATES=[
        # Django 1.8 starter-project template settings
        # (needed for test_admin)
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                # insert your TEMPLATE_DIRS here
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'countries_plus.context_processors.add_request_country',
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
    # For Django <1.8
    TEMPLATE_CONTEXT_PROCESSORS=('countries_plus.context_processors.add_request_country',
                                 "django.contrib.auth.context_processors.auth",
                                 "django.template.context_processors.debug",
                                 "django.template.context_processors.i18n",
                                 "django.template.context_processors.media",
                                 "django.template.context_processors.static",
                                 "django.template.context_processors.tz",
                                 "django.contrib.messages.context_processors.messages"),
    # countries_plus settings
    COUNTRIES_PLUS_COUNTRY_HEADER='GEOIP_HEADER',
    COUNTRIES_PLUS_DEFAULT_ISO='US'
)
# Django 1.7+ initialize app registry
from django import setup

setup()

try:
    from django.test.runner import DiscoverRunner as TestRunner  # Django 1.6+
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner as TestRunner  # Django -1.5


def runtests():
    test_runner = TestRunner(verbosity=1)
    failures = test_runner.run_tests([APP])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
