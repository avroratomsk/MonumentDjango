from .settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = [
    # "django.contrib.admin",
    "admin",
    'accounts',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_ckeditor_5',
    "debug_toolbar",
    # "corsheaders",
    'sorl.thumbnail',
    'django.contrib.sitemaps',
    "home",
    "shop",
    # "coupons",
    "users",
    "service",
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'tinymce',
    "blog",
    "news",
    "branch",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
#     'allauth.account.middleware.AccountMiddleware',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'C:/Users/sania/project/dj-artflora/main/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
        },
        'myapp_test': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    }
}