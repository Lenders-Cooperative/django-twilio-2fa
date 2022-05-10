"""
Django settings for test_app project.
Generated by 'django-admin startproject' using Django 3.1.7.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()

environ.Env.read_env(
    BASE_DIR / "test_app" / ".env"
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "uhtgm(e2y3@5%0x!wy#re#fn+51h*ck88^ocm7d1=hx^@(&7$7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #
    "widget_tweaks",
    "django_twilio_2fa.apps.Twilio2faConfig",
    #
    "users.apps.UsersConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "test_app.middleware.Require2faMiddleware",
]

ROOT_URLCONF = "test_app.urls"

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

WSGI_APPLICATION = "test_app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

# DJANGO-TWILIO-2FA

TWILIO_2FA_ACCOUNT_SID = env("TWILIO_2FA_ACCOUNT_SID")
TWILIO_2FA_AUTH_TOKEN = env("TWILIO_2FA_AUTH_TOKEN")
TWILIO_2FA_SERVICE_ID = env("TWILIO_2FA_SERVICE_ID")

TWILIO_2FA_ALLOWED_METHODS = None

def twilio_2fa_register_cb(user, phone_number):
    from users.models import UserProfile

    if not hasattr(user, "profile"):
        user.profile = UserProfile.objects.create(
            user=user
        )

    user.profile.phone_number = phone_number
    user.profile.save()

    return True

TWILIO_2FA_REGISTER_CB = twilio_2fa_register_cb

def twilio_2fa_phone_number(user=None):
    if user and hasattr(user, "profile"):
        return user.profile.phone_number

    return None

TWILIO_2FA_PHONE_NUMBER_CB = twilio_2fa_phone_number

TWILIO_2FA_ALLOW_CHANGE = False
