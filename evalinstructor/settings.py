import os
import json
from pathlib import Path
from .dbases import *
from .confSett import localSett, prodSett, securFileHome, securFileSena

SENA = False

if SENA:
    config = securFileSena()
else:
    config = securFileHome()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config['SECRET_KEY']

DEBUG = True

if DEBUG == True:
    ALLOWED_HOSTS, INSTALLED_APPS = localSett()
else:
    ALLOWED_HOSTS, INSTALLED_APPS = prodSett()

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'evalinstructor.urls'

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

WSGI_APPLICATION = 'evalinstructor.wsgi.application'

DATABASES = {
    'default': {},
    'users_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "dbs/users.db"),
    },
    'staff_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "dbs/staff.db"),
    },
    'testings_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "dbs/testings.db"),
    },
}

DATABASE_ROUTERS = ['routers.db_routers.AuthRouter', 'routers.db_routers.StaffRouter', 'routers.db_routers.TestingsRouter',]

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