"""Common settings and globals."""
from os.path import abspath, basename, dirname, join, normpath
from sys import path


########## PATH CONFIGURATION
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## HTTPS CONFIGURATION
"""This will break a non-https site"""
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
######### END HTTPS CONFIGURATION


########## MANAGER CONFIGURATION
ADMINS = (
    ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## GENERAL CONFIGURATION
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
STATIC_ROOT = normpath(join(SITE_ROOT, 'collectstatic'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## FIXTURE CONFIGURATION
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 'django.contrib.admin', (Third Party, order matters)
    'django.contrib.sitemaps',
)

THIRD_PARTY_APPS = (
    'south',
    'sorl.thumbnail',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'tinymce',
)

LOCAL_APPS = (
    'blog',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


######### TINY MCE
TINYMCE_JS_URL = normpath(join(MEDIA_URL, "js/tiny_mce/tiny_mce.js"))
TINYMCE_DEFAULT_CONFIG = {
    'theme': "simple",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False
######## END TINY_MCE


#### SORL-THUMBNAIL
THUMBNAIL_QUALITY = 70
THUMBNAIL_PROGRESSIVE = True
##### END SORL-THUMBNAIL

########## GRAPPELLI CONFIGURATION
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.DashboardIndex'
GRAPPELLI_ADMIN_TITLE = "{{ project_name }}"
########## END GRAPPELLI CONFIGURATION


########## LOGGING CONFIGURATION
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION
