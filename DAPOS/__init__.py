# TODO: Copyrights, license Documentation
"""
This is the root package responsible for:
    1- configuring django as a library to use some stand-alone features:
        1- django ORM
        2- models object caching
        3- models object serialization
        4- fixtures
"""
import os
from django.conf import settings

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(PROJECT_ROOT, 'data/DAPOS.db')
        }
    },
    FIXTURE_DIRS=(os.path.join(PROJECT_ROOT, 'data/fixtures'),),
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': os.path.join(PROJECT_ROOT, 'memcached.sock'),
        }
    },
    INSTALLED_APPS=('DAPOS.data',),
)
