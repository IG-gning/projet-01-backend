"""
Django settings pour Render + frontend Vercel + Cloudinary
"""

from pathlib import Path
import os
import dj_database_url


# --------------------------
# Chemins
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------
# Sécurité
# --------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-default-key")


# Nouveau (temporaire pour debug) :
DEBUG = True


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "projet-01-backend-1.onrender.com",
    "front-end-mu-six.vercel.app",
]

# --------------------------
# Applications installées
# --------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'inscription',
    'forms_app',
    'messages_app',
    'hotels',
    'entrees',

    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",

    "cloudinary",
    "cloudinary_storage",
]

# --------------------------
# REST Framework + JWT
# --------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# --------------------------
# Middleware
# --------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------
# CORS et CSRF
# --------------------------
CORS_ALLOWED_ORIGINS = [
    "https://front-end-mu-six.vercel.app",
]
CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    "https://front-end-mu-six.vercel.app",
]

# --------------------------
# URLs et templates
# --------------------------
ROOT_URLCONF = 'hotel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hotel.wsgi.application'

# --------------------------
# Base de données PostgreSQL Render
# --------------------------
if os.environ.get("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "hotel",
            "USER": "postgres",
            "PASSWORD": "idy1234",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }

# --------------------------
# Password validators
# --------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------
# Internationalisation
# --------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------
# Fichiers statiques et media
# --------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------
# Sécurité supplémentaire
# --------------------------
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

import cloudinary
cloudinary.config(
    cloud_name='dtsfv5tfm',
    api_key='157261688994592',
    api_secret='EglL47pRqv6-nUlYVtYOadKiJ5U',
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dtsfv5tfm',
    'API_KEY': '157261688994592',
    'API_SECRET': 'EglL47pRqv6-nUlYVtYOadKiJ5U',
}
