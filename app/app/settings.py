"""Django settings for app project"""

from pathlib import Path

import environ
from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    # Third-party
    "debug_toolbar",
    # Apps
    "app",
    "main.apps.MainConfig",
    "goods.apps.GoodsConfig",
    "users.apps.UsersConfig",
    "carts.apps.CartsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Third-party
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "app.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": env('POSTGRES_DB'),
        "USER": env('POSTGRES_USER'),
        "PASSWORD": env('POSTGRES_PASSWORD'),
        "HOST": env('POSTGRES_HOST'),
        "PORT": env('POSTGRES_PORT', default=5432),
    }
}

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

# Project incide settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media files
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Debug toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Settings
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.User"
LOGIN_URL = "/user/login/"
