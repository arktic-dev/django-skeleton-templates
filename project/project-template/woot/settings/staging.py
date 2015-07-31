# {{project_name}}.settings.staging

# django
# local
from woot.settings.common import *

# util
from os import environ

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########### DATABASE CONFIGURATION
# load database details from database config file
if os.path.exists(os.path.join(ACCESS_ROOT, DB_ACCESS)):
  with open(os.path.join(ACCESS_ROOT, DB_ACCESS), 'r') as db_json:
    db_data = json.loads(db_json)

DATABASES = {
  'default': {
    'ENGINE': db_data['backend'],
    'NAME': db_data['name'],
    'USER': db_data['user'],
    'PASSWORD': db_data['pwd'],
    'HOST': db_data['host'], # Set to empty string for localhost.
    'PORT': db_data['port'], # Set to empty string for default.
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
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = '{{ secret_key }}'
########## END SECRET CONFIGURATION


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

DEBUG_TOOLBAR_CONFIG = {

}
########## END TOOLBAR CONFIGURATION
