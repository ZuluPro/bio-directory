import os

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = '&qaeg(m5s0rpdj-wx@hrc3vpu)v@@n$if67ba-4e9&kk+j$$c+'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/test-bio.sqlite',
    },
}

SECRET_KEY = "django_bio_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'schedule',
    'bio',
    'bio.guide',
    'bio.items',
    'bio.scheduler',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/tmp/media/')

ROOT_URLCONF = 'bio.tests.urls'
