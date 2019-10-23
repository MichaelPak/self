from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ('POSTGRES_DB'),
        'USER': os.environ('POSTGRES_USER'),
        'PASSWORD': os.environ('POSTGRES_PASSWORD'),
        'HOST': os.environ('POSTGRES_HOST'),
        'PORT': os.environ('POSTGRES_PORT'),
    }
}
