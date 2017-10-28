"""
Django settings for medical_prescription project.
Generated by 'django-admin startproject' using Django 1.11.4.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from decouple import config
from dj_database_url import parse as dburl
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kw&cp#em42$66%lprfln@!25t%(wb9j4gzz%vxaah(v-e8zxbt'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['medicalprescription.herokuapp.com', 'localhost', '127.0.0.1', '0.0.0.0']


# Set initial database


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'medicine',
    'user',
    'landing',
    'dashboardPatient',
    'dashboardHealthProfessional',
    'exam',
    'disease',
    'prescription',
    'chat',
]

# ====== DONT REMOVE -ME
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'medicalprescriptionapp@gmail.com'
EMAIL_HOST_PASSWORD = 'medicalprescription123'
EMAIL_PORT = 587


# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'codamaisapp@gmail.com'
# EMAIL_HOST_PASSWORD = 'codamais'
# EMAIL_PORT = 587

AUTH_USER_MODEL = "user.User"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

LANGUAGES = (
    ('en', _('English')),
    ('pt-br', _('Portuguese (Brazil)')),
)

# Locale Path for translation
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

ROOT_URLCONF = 'medical_prescription.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            'medical_prescription/templates',
            'landing/templates',
            'user/templates',
            'dashboardPatient/templates',
            'dashboardHealthProfessional/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors':
            [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'medical_prescription.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost'
        }
    }
elif 'DYNO' in os.environ:
    default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'db',
            'PORT': 5432,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
LOGIN_URL = '/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
