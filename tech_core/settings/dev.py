from tech_core.settings.base import *  # noqa: F403

# Database settings
if config("DB_TYPE", default="") == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }



MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware", *MIDDLEWARE]

INSTALLED_APPS += [
    "debug_toolbar",
    'django_extensions',
]

# CLI attrs for django_extensions: https://django-extensions.readthedocs.io/en/latest/graph_models.html#default-settings
GRAPH_MODELS = {
  'app_labels': ["cart", "checkout", "core", "order", "product", "users"],
}

# Allauth settings
ACCOUNT_RATE_LIMITS = False

# SMTP settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
