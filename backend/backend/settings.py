"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!23&j165oclm&!cm8j(u39aqauqnp(d3=pmd5-)izne@&^gu3n"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ALLOWED_HOSTS = (
#     '192.168.1.70',
#     'localhost',
#     'localhost:8000',
#     'localhost:5000',
#     '.localapp.com',
#     '.app.com',
#     '.staging.com',
# )


# CORS_ORIGIN_REGEX_WHITELIST = [
#     r"http://\w+\.\w+\.localapp\.com:8000$",
#     r"http://\w+\.localapp\.com:8000$",
#     r"http://<slug>.\w+\.localapp\.com:8000$",
#     r"http://<slug>.localapp\.com:8000$",
#     r"http://localhost:10001$",
#     r"https://\w+\.app\.com$",
#     r"https://\w+\.\w+\.app\.com$",
#     r"https://\w+\.\w+\.appstaging\.com$",
#     r"https://\w+\.appstaging\.com$",
#     r"https://<slug>.\w+\.appstaging\.com$",
#     r"https://<slug>.appstaging\.com$",
#     r"https://localhost:10001$",
#     r"https://\w+\.appstaging\.com$",
#     r"https://\w+\.\w+\.appstaging\.com$",
#     r"null",
# ]

# CORS_ALLOW_CREDENTIALS = True
#from corsheaders.defaults import default_headers
# CORS_ALLOW_HEADERS = default_headers + (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'Oto-Org',
#     'Oto-Location',
#     'x-csrftoken',
#     'x-requested-with',
# )
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders", #1
    "apis",
    "accounts",
]

CORS_ALLOWED_ORIGINS = ['http://192.168.2.15:3000', 'http://localhost:3000'] #'http://localhost:5173', #2

AUTH_USER_MODEL = "accounts.User" #specify custom user model
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware', #3
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apis.middleware.ApiMiddleware",
]

ROOT_URLCONF = "backend.urls"

REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "errors", #remove non-field errors
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100 
}

SIMPLE_JWT= {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=99),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    

}
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
