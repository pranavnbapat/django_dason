import os
from pathlib import Path
from django.contrib.messages import constants as messages
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]
LOCAL_APPS = [
    "pages",
    # "backend",
    "backend.apps.BackendConfig",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",

    # Configure the django-otp package.
    "django_otp",
    "django_otp.plugins.otp_totp",
    "django_otp.plugins.otp_static",

    # Enable two-factor auth.
    "allauth_2fa",
    "django_extensions",

    # REST framework
    "rest_framework",
    "rest_framework.authtoken",

    # For elastic search on long columns
    "django_elasticsearch_dsl",

    # For rate-limit on failed password attempts
    "axes",

    # For tweaking built-in widgets
    "widget_tweaks",
]

AUTH_USER_MODEL = 'backend.DefaultAuthUserExtend'

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Custom middlewre to track user activity
    "euf.middleware.UserActivityMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # AuthenticationMiddleware.
    "django_otp.middleware.OTPMiddleware",
    # Reset login flow middleware. If this middleware is included, the login
    # flow is reset if another page is loaded between login and successfully
    # entering two-factor credentials.
    "allauth_2fa.middleware.AllauthTwoFactorMiddleware",
    "axes.middleware.AxesMiddleware",
    "csp.middleware.CSPMiddleware",
]

CSP_INCLUDE_NONCE_IN = ('script-src', 'style-src')
CSP_IMG_SRC = ("'self'", "data:")
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://fonts.googleapis.com",)
CSP_CONNECT_SRC = ("'self'", "http://localhost:27017",)
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com", "https://fonts.googleapis.com",)
CSP_MEDIA_SRC = ("'self'",)

# Extra layers of security
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True # This can be implemented once the site is HTTPS

ACCOUNT_ADAPTER = "allauth_2fa.adapter.OTPAdapter"

ROOT_URLCONF = "euf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                "django.template.context_processors.request",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # For failed password attempts rate limit
    "axes.backends.AxesStandaloneBackend",
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# AXES_FAILURE_LIMIT = 5  # Number of failed login attempts before lockout
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True  # Lockout based on the combination of user and IP address
AXES_LOCKOUT_FUNCTION = 'euf.axes_handlers.custom_lockout_time'
# AXES_COOLOFF_TIME = 60
AXES_RESET_ON_SUCCESS = True
AXES_LOG_ACCESS_ATTEMPTS = True
AXES_LOG_ACCESS_FAILURE_ATTEMPTS = True
AXES_LOG_FAILURE_ATTEMPTS = True

WSGI_APPLICATION = "euf.wsgi.application"

ASGI_APPLICATION = 'euf.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("MYSQL_DB"),
        'USER': os.getenv("MYSQL_USER"),
        'PASSWORD': os.getenv("MYSQL_PASS"),
        'HOST': os.getenv("MYSQL_HOST"),
        'PORT': os.getenv("MYSQL_PORT"),
    },
}

MONGO_CLIENT = MongoClient(
    host=os.getenv("MONGODB_HOST"),
    port=int(os.getenv("MONGODB_PORT")),
    username=os.getenv("MONGODB_USER"),
    password=os.getenv("MONGODB_PASS"),
    authSource=os.getenv("MONGODB_DB"),
    authMechanism='SCRAM-SHA-1',
)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

AVATAR_PATH = BASE_DIR / "media/images/users"
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


# SMTP Configure
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

CRISPY_TEMPLATE_PACK = "bootstrap4"


LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = "/backend/dashboard/"
LOGOUT_REDIRECT_URL = "/backend/dashboard/"
ACCOUNT_LOGOUT_REDIRECT_URL = '/backend/dashboard/'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"


SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}
# To Customised Forms fields style
ACCOUNT_FORMS = {
    "login": "euf.forms.UserLoginForm",
    "signup": "euf.forms.UserSignupForm",
    "reset_password": "euf.forms.UserResetPasswordForm",
    "reset_password_from_key": "euf.forms.UserResetPasswordKeyForm",
    "change_password": "euf.forms.UserChangePasswordForm",
    "set_password": "euf.forms.UserSetPasswordForm",
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# Storage path for PDF2TEXT
STORAGE_DIR = os.path.join(BASE_DIR, 'storage')
PDF2TEXT_PATH = os.path.join(STORAGE_DIR, 'pdf2text')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'https://localhost:9200',  # or the address of your Elasticsearch instance
        'http_auth': ('elastic', 'asdasdasd'),
        'verify_certs': False,
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'user_activity.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'backend.models': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


