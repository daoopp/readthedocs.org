from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'docs',
        'USER': 'postgres',                      # Not used with sqlite3.
        'PASSWORD': '',
        'HOST': '10.177.73.97',
        'PORT': '',
    }
}

DEBUG = False
TEMPLATE_DEBUG = False
CELERY_ALWAYS_EAGER = False

MEDIA_URL = '//media.readthedocs.org/'
STATIC_URL = '//media.readthedocs.org/static/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://odin:8983/solr',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'PREFIX': 'docs',
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}

SLUMBER_API_HOST = 'https://readthedocs.org'
WEBSOCKET_HOST = 'websocket.readthedocs.org:8088'

PRODUCTION_URL = 'readthedocs.org'
USE_SUBDOMAIN = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")



try:
    from local_settings import *
except:
    pass
