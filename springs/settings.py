"""
Django settings for springs project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import dotenv
from dotenv import load_dotenv
dotenv.load_dotenv()
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7v&ph%=o3ap5c5ap2=*)2isf2a#qy#+_l9a^dx7!zlg$b+)ox7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost","spol.herokuapp.com","www.springsoflifeg.com"]


# Application definition

INSTALLED_APPS = [
    # 'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Other Apps
    'sol',
    'crispy_forms',
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

ROOT_URLCONF = 'springs.urls'




CRISPY_TEMPLATE_PACK = 'bootstrap3'



os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.join(BASE_DIR, 'springs-8a71d8f7389e.json')




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'springs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
import dj_database_url
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 2525
EMAIL_HOST_USER = os.getenv('EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_TIMEOUT = 30
EMAIL_USE_TLS = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


if  DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        #'/var/www/static/',
    ]
    STATIC_URL = '/static/'
    OUTREACH="outreach"
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT=os.path.join(BASE_DIR,'media')




else:
    OUTREACH="outreach"
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    # DEFAULT_FILE_STORAGE = 'storages.backends.gs.GSBotoStorage'
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    # GS_ACCESS_KEY_ID =os.getenv("CLIENT_ID")
    # GS_SECRET_ACCESS_KEY = os.getenv("CLIENT_SECRET")
    GS_BUCKET_NAME = "springs" #os.getenv("GCS_BUCKET")
    # GS_PROJECT_ID = os.getenv("GCLOUD_PROJECT")
    STATIC_ROOT = "https://storage.googleapis.com/springs/static"
    STATIC_URL = 'https://storage.googleapis.com/springs/'
    MEDIA_URL = 'https://storage.googleapis.com/springs/media/'
    DATABASES = {
    'default': dj_database_url.config(
        default='DATABASE_URL'
    )
}