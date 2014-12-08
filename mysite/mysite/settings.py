"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR,'templates/').replace('\\','/')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'le(yd(e06#fc=k_=0d&)o$uu1m6$2u$!r$vh8vr&m_f!c*$968'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# SESSION_SAVE_EVERY_REQUEST = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django,middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static/').replace('\\','/') ]

#memcache
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION':'127.0.0.1:11211',
	}
}

#database caching
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.db.DatabaseCache',
		'LOCATION':'my_cache_table',
	}
}

#filesystem caching
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
		'LOCATION':'/vagrant/tmp/django_cache',
	}
}
#local-memory caching
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
		'LOCATION':'unique-snowflake'
	}
}
#dummy caching
CACHES = {
	'default':{
		'BACKEND':'django.core.cache.backends.dummy.DummyCache',
	}
}
