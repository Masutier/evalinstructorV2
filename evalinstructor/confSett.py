import os
import json


def localSett():
    ALLOWED_HOSTS = ['localhost']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'evalinstructor',
        'loadings',
        'testings',

    ]

    return ALLOWED_HOSTS, INSTALLED_APPS


def prodSett():
    ALLOWED_HOSTS = ['url hosting']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'evalinstructor',
        'loadings',
        'testings',

    ]

    return ALLOWED_HOSTS, INSTALLED_APPS


def securFileHome():
    with open("/home/gabriel/prog/json_config/senadlake.json") as config_file:
        config = json.load(config_file)
    return config


def securFileSena():
    with open("/etc/senadlake.json") as config_file:
        config = json.load(config_file)
    return config
