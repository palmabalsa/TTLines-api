"""
Django settings for tight_lines project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from telnetlib import AUTHENTICATION
from datetime import timedelta
import firebase_admin
from firebase_admin import credentials
import os
from decouple import config
import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# changed this to false to test the api with my flutter app!
DEBUG = config('DEBUG')




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'troutApi',
    'social_django',
    'trout',
    'conditions',
    'rest_framework',
    'corsheaders',
    'users',
    'django_extensions'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tight_lines.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
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

WSGI_APPLICATION = 'tight_lines.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
     'default' : {
         'ENGINE' : 'django.db.backends.postgresql',
         'NAME' : config('DB_NAME'),
         'USER' : config('DB_USER'),
         'PASSWORD' : config('DB_PASS'),
         'HOST' : '127.0.0.1',
         'PORT' : '5432',
     }    
}

AUTH_USER_MODEL = 'users.User'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
# ACCOUNT_FORMS = {'signup': 'users.forms.CustomUserCreationForm'}



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NB!!! make sure that you get the proper reqs for psychopg if this goes into productuion, atm
# only useing psycopg binary version, need to add aditional things to be able to use it properly!!!!
# this is for pgadmin






# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Pacific/Auckland'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTH0 SETTINGS:
# SOCIAL_AUTH_TRAILING_SLASH = False
# SOCIAL_AUTH_AUTH0_DOMAIN = 'dev-lmvb9vwu.au.auth0.com'
# SOCIAL_AUTH_AUTH0_KEY = 'HLp019HZlWzxPxstrMspRhoRhjJSwI5C'
# SOCIAL_AUTH_AUTH0_SECRET = 'UyEzrtyGVWo499BunNf3kemhQcrrv_ldlwg52U-75aQsWQAp3Nj-LC5bbXZQ2_wn'
# SOCIAL_AUTH_AUTH0_SCOPE = ['openid', 'profile', 'email']

AUTHENTICATION_BACKENDS = {
    # 'social_core.backends.auth0.Auth0OAuth2',
    'django.contrib.auth.backends.ModelBackend',
}

LOGIN_URL ='/login/'
LOGIN_REDIRECT_URL = '/catchdata'
LOGOUT_REDIRECT_URL = '/'


REST_FRAMEWORK = {
    'DATE_INPUT_FORMATS' : [("%d-%m-%Y"), "iso-8601"],
    'DATETIME_INPUT_FORMATS' : ["iso-8601"],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'users.backends.FirebaseBackend',
        'users.backends.JWTAuthentication',
        "rest_framework.authentication.SessionAuthentication",
        
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
     
}

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1",
    "http://localhost",
    "http://localhost:55555",
    "https://tight-lines-app.herokuapp.com",
]

CORS_ORIGIN_ALLOW_ALL = True


CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


ALLOWED_HOSTS = ['*']
# '0.0.0.0', '192.168.20.102', 'localhost', '127.0.0.1',


cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": config('FIREBASE_PROJECT_ID'),
        "private_key_id": config('FIREBASE_PRIVATE_KEY_ID'),
        "private_key": config('FIREBASE_PRIVATE_KEY').replace('\\n','\n'),
        "client_email": config('FIREBASE_CLIENT_EMAIL'),
        "client_id": config('FIREBASE_CLIENT_ID'),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": config('FIREBASE_CLIENT_x509_CERT_URL'),
    }
)

# FIREBASE_APP = firebase_admin.initialize_app(cred)
firebase_admin.initialize_app(cred)

django_heroku.settings(locals())







