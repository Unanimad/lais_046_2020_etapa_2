import dj_database_url

from vaccine_card.core.settings.base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

DEBUG = False
DATABASE_URL = os.environ.get('DATABASE_URL', '')
DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
