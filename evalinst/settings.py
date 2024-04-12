import os, json
from pathlib import Path
from .confsett import localSett, prodSett


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# usar DEBUG = False si la app esta en desarrollo
# usar DEBUG = True si la app esta en produccion

if DEBUG == True:
    config, ALLOWED_HOSTS, INSTALLED_APPS, DATABASES = localSett(BASE_DIR)
else:
    config, ALLOWED_HOSTS, INSTALLED_APPS, DATABASES = prodSett(BASE_DIR)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'evalinst.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'evalinst.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587    # smtp server port if TLS = 587, or SSL = 465
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'cpsi.inhouse52@gmail.com'
EMAIL_HOST_PASSWORD = config['EMAIL_PASSWORD']

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Bogota'
# DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S' 
USE_I18N = True
USE_L10N = True
USE_TZ = True

# PRODUCTION
STATIC_ROOT = os.path.join(BASE_DIR, "/static/")
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

SESSION_COOKIE_AGE = 21600
SESSION_COOKIE_SAMESITE = None
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = False
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
