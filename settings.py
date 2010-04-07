# Django settings for project.
import os
import django
import sys

# Path of Django framework files (no trailing /):
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
# Path of this "site" (no trailing /):
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q_ou*rndj_kcfnq5*#$od0923q&r99w+lrhfbowunxat5y#l^g'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django_fakewall.middleware.FakewallMiddleware', #maintenance mode
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes', #required by auth
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'annoying', #django-annoying
    'south', #migrations
    'django_rpx_plus', 
    #'celery', #messaging queue
    'app', #make sure to rename this
)

#The following is not in the default generated settings.py file:

AUTHENTICATION_BACKENDS = (
    'django_rpx_plus.backends.RpxBackend', 
    'django.contrib.auth.backends.ModelBackend', #default django auth
    #'app.backends.CustomPermBackend', #if we want obj-level perm
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request', #for request object
    'django.contrib.messages.context_processors.messages',
    #Above are the default template context processors
    #'app.helpers.context_processor',
)

#Additional user data (ie. User Profile)
#AUTH_PROFILE_MODULE = 'base.UserProfile'

# Here are some settings related to auth urls. django has default values for them
# as specified on page: http://docs.djangoproject.com/en/dev/ref/settings/. You
# can override them if you like.
#LOGIN_REDIRECT_URL = '' #default: '/accounts/profile/'
#LOGIN_URL = '' #default: '/accounts/login/'
#LOGOUT_URL = '' #default: '/accounts/logout/'

####################
# app settings:    #
####################

#Put all of your app settings here.


####################
# celery settings: #
####################

#CELERY_BACKEND = 'database' #default = database

#BROKER_HOST = 'localhost'
#BROKER_PORT = 5672
#BROKER_USER = 'dev'
#BROKER_PASSWORD = 'testtest'
#BROKER_VHOST = 'mXs-MBP'

#If True, tasks are executed locally and never sent to queue.
#CELERY_ALWAYS_EAGER = True
#CELERYD_LOG_LEVEL = 'INFO'

############################
#django_rpx_plus settings: #
############################
#RPXNOW_API_KEY = ''

# The realm is the subdomain of rpxnow.com that you signed up under. It handles 
# your HTTP callback. (eg. http://mysite.rpxnow.com implies that RPXNOW_REALM  is
# 'mysite'.
RPXNOW_REALM = ''

# (Optional)
RPX_TRUSTED_PROVIDERS = ''

# (Optional)
# RPX requires a token_url to be passed to its APIs. The token_url is an
# absolute url that points back to the rpx_response view. By default, this
# token_url is constructed by using request.get_host(). However, there may
# be cases where rpx_response is hosted on another domain (eg. if the website
# is using subdomains). Therefore, we can force the base url to be fixed instead
# of auto-detected. 
# Note: This is the HOSTNAME without the beginning 'http://' or trailing slash
#       part. An example hostname would be: localhost:8000
# Protip: You can set RPX_BASE_SITE_HOST in middleware too.
#RPX_BASE_SITE_HOST = '' #Set in middleware

# If it is the first time a user logs into your site through RPX, we will send 
# them to a page so that they can register on your site. The purpose is to 
# let the user choose a username (the one that RPX returns isn't always suitable)
# and confirm their email address (RPX doesn't always return the user's email).
REGISTER_URL = '/accounts/register/'


#Import any local settings (ie. production environment) that will override
#these development environment settings.
try:
    from local_settings import *
except ImportError:
    pass 
