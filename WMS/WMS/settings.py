# -*- coding:utf-8 -*-
import os

from .settings_django_suit import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fli=(wbzw+o^_8nxqb1!01*byehw39p%d+@=&mje4(v2&x_h6a'

DEBUG = False

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    # 'suit',
    'django_suit.apps.SuitConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 业务app
    'base.apps.BaseConfig',
    'users.apps.UsersConfig',
    'records.apps.RecordsConfig',
    'products.apps.ProductsConfig',
    'salary.apps.SalaryConfig',
    'wechat.apps.WechatConfig',
    'testing.apps.TestingConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
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

WSGI_APPLICATION = 'WMS.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'wms',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USER_GROUP = {
    1: u'办公室',
    2: u'裁剪组',
    3: u'缝纫组',
    4: u'熨烫组',
    5: u'包装组',
    6: u'运输组',
    7: u"日工",
}

BROKER_URL = 'redis://localhost:6379/'

STATIC_URL = '/django-static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
