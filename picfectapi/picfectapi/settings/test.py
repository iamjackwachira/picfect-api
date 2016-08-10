from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'test.db')
    }
}
MEDIA_ROOT = os.path.abspath('test_media')
MEDIA_URL = '/media/'
