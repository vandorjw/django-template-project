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

########## HOST CONFIGURATION
ALLOWED_HOSTS = []
########## END HOST CONFIGURATION


####
DEBUG = False
TEMPLATE_DEBUG = DEBUG
####


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_setting('{{ project_name }}_DB_NAME'),
        'USER': get_env_setting('{{ project_name }}_DB_USER'),
        'PASSWORD': get_env_setting('{{ project_name }}_DB_PASS'),
        'HOST': get_env_setting('{{ project_name }}_DB_HOST'),
        'PORT': get_env_setting('{{ project_name }}_DB_PORT'),,
    }                                             
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
SECRET_KEY = get_env_setting('{{ project_name }}_SECRET_KEY'
########## END SECRET CONFIGURATION
