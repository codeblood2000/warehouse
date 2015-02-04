import os
import sys

#import djcelery
#djcelery.setup_loader()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, PROJECT_ROOT)

ADMINS = (
    ('Steven Challis', 'steve@stevechallis.com'),
)

MANAGERS = ADMINS

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'warehouse',
        'USER': 'stevenchallis',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '((@b3f+s!o8^r$wb$p8@+&8k@&y*3o7sy3dp4xk+45=$e2996x'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'warehouse.urls'

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'djcelery',
    'reporting',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {},
    'loggers': {
        'django.request': {
            'handlers': [],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

VIDISPINE_REPLACE_URLS = ''
VIDISPINE_URL = 'http://dev-vidi'
VIDISPINE_PORT = '8080'
VIDISPINE_USERNAME = 'admin'
VIDISPINE_PASSWORD = 'goose'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

#CELERY SETTINGS
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"

DAM_MANAGER_CLASS = "BorkAssetQuerySet"
