import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Security
SECRET_KEY = 'tempkey'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Apps (CRITICAL ORDER)
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # MUST BE FIRST
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'products',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... other middleware ...
]

# Static Files (WINDOWS-SPECIFIC)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))  # Normalized path
STATICFILES_DIRS = [os.path.normpath(os.path.join(BASE_DIR, 'static'))]  # Normalized path

# Storage
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",  # No Manifest
    },
}

WHITENOISE_KEEP_ONLY_HASHED_FILES = False  # Disable hashing

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # If using os.path