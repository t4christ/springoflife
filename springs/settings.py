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

# ALLOWED_HOSTS = ["localhost","192.168.99.100","spol.herokuapp.com","www.springsoflifeg.com"]
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Other Apps
    'sol',
    'paystack',
    'posts',
    'taggit',
    'comments',
    'pagedown',
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



# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.join(BASE_DIR,'spgoflife-c8c96ccea7e8.json')




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


if not DEBUG:

    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('POSTGRES_DATABASE'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'PORT': os.environ.get('POSTGRES_PORT'),
        }
    }


EMAIL_HOST=os.environ.get('SMARTHOST_ADDRESS')
EMAIL_PORT=os.environ.get('SMARTHOST_PORT')
EMAIL_HOST_USER=os.environ.get('SMARTHOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('SMARTHOST_PASSWORD')
EMAIL_TIMEOUT = 30
EMAIL_USE_TLS = True



# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = os.environ.get('EMAIL_USERNAME')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
# EMAIL_TIMEOUT = 30
# EMAIL_USE_TLS = False




PAYSTACK_PUBLIC_KEY=os.environ.get('PAYSTACK_PUBLIC_KEY')
PAYSTACK_SECRET_KEY=os.environ.get('PAYSTACK_SECRET_KEY')
# PAYSTACK_FAILED_URL='failed-verification'
# PAYSTACK_SUCCESS_URL='successful-verification'
PAYSTACK_WEBHOOK_DOMAIN='http://5eeab2a8.ngrok.io'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


if  DEBUG:

    STATIC_DIR = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
    STATIC_DIR,
    ]
    POST_URL='posts'
    PROFILE_URL='profile_photo'
    OUTREACH="outreach"
    MEDIA_URL = '/media/'
    MEDIA_ROOT=os.path.join(BASE_DIR,'media')




else:
    OUTREACH="outreach"
    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = 'static'
    STATICFILES_LOCATION = 'storages.backends.s3boto3.S3Boto3Storage'
'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'


#     DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#     # DEFAULT_FILE_STORAGE = 'storages.backends.gs.GSBotoStorage'
#     STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#     # GS_ACCESS_KEY_ID =os.getenv("CLIENT_ID")
#     # GS_SECRET_ACCESS_KEY = os.getenv("CLIENT_SECRET")
#     GS_BUCKET_NAME = "spgoflife" #os.getenv("GCS_BUCKET")
#     # GS_PROJECT_ID = os.getenv("GCLOUD_PROJECT")
#     STATIC_ROOT = "https://storage.googleapis.com/spgoflife/static"
#     STATIC_URL = 'https://storage.googleapis.com/spoflife/'
#     MEDIA_URL = 'https://storage.googleapis.com/spgoflife/media/'
#     DATABASES = {
#     'default': dj_database_url.config(
#         default='DATABASE_URL'
#     )
# }