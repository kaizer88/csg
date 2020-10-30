import os
from .settings import *


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'csg',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                      # Not used with sqlite3.
        # 'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'Lihle@2016',                  # Not used with sqlite3.
        # 'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        # 'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    },
    # 'splicedb': {
    #         # 'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    #         'NAME': 'myhome',                      # Or path to database file if using sqlite3.
    #         'USER': 'postgres',                      # Not used with sqlite3.
    #         # 'USER': 'root',                      # Not used with sqlite3.
    #         'PASSWORD': 'Lihle@2016',                  # Not used with sqlite3.
    #         # 'PASSWORD': '',                  # Not used with sqlite3.
    #         'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
    #         # 'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    #         'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    #     }

}

ALLOWED_HOSTS = []


EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

TIME_ZONE = 'Africa/Johannesburg'


try:
    from .local_settings import *
except ImportError:
    pass