"""Development settings and globals."""
from os.path import join, normpath
from os import environ
from base import *
from django.core.exceptions import ImproperlyConfigured

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# Sorl-Thumbnail Option
THUMBNAIL_DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_PASSWORD = get_env_setting('{{ project_name }}_EMAIL_PASS')
EMAIL_HOST_USER = get_env_setting('{{ project_name }}_EMAIL_USER')
EMAIL_HOST = get_env_setting('{{ project_name }}_EMAIL_HOST')
EMAIL_PORT = get_env_setting('{{ project_name }}_EMAIL_PORT')
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_setting('{{ project_name }}_DB_NAME'),
        'USER': get_env_setting('{{ project_name }}_DB_USER'),
        'PASSWORD': get_env_setting('{{ project_name }}_DB_PASS'),
        'HOST': get_env_setting('{{ project_name }}_DB_HOST'),
        'PORT': get_env_setting('{{ project_name }}_DB_PORT'),
    }                                             
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
########## END TOOLBAR CONFIGURATION
