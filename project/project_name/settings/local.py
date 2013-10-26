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
DEBUG = True
THUMBNAIL_DEBUG = True
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
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
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
INSTALLED_APPS += (
    'debug_toolbar',
)
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
########## END TOOLBAR CONFIGURATION

########## SECRET CONFIGURATION
SECRET_KEY = get_env_setting('{{ project_name }}_SECRET_KEY')
########## END SECRET CONFIGURATION
