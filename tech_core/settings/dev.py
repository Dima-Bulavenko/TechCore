from tech_core.settings.base import *  # noqa: F403

# Allauth settings
ACCOUNT_RATE_LIMITS = False

# SMTP settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
