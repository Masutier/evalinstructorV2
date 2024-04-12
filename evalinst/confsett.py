import os, json
from django.conf import settings


def localSett(BASE_DIR):
    # entorno de desarrollo
    with open("/home/gabriel/prog/json_config/evalinstructor.json") as config_file:
        config = json.load(config_file)
    
    ALLOWED_HOSTS = ['localhost']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'evalinst',
        'loadlist',
    ]
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, "dbs/evalinst.db"),
        }
    }
    return config, ALLOWED_HOSTS, INSTALLED_APPS, DATABASES


def prodSett(BASE_DIR):
    # entorno de produccion
    with open("/etc/evalinstructor.json") as config_file:
        config = json.load(config_file)

    ALLOWED_HOSTS = ['url hosting', '172.17.125.17']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'evalinst',
        'loadlist',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'evalinstructores',
            'USER': config["MARIADB_USER"],
            'PASSWORD': config["MARIADB_PASSWORD"],
            'HOST': 'localhost',
            'PORT': int(config["MARIADB_PORT"]),
        }
    }

    return config, ALLOWED_HOSTS, INSTALLED_APPS, DATABASES

