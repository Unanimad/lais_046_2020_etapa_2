import os

from vaccine_card.core.settings.base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lais',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': '16031994'
    }
}
