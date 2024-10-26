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
]
# Allauth settings
ACCOUNT_RATE_LIMITS = False

# SMTP settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
