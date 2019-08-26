import os
import dj_database_url
import django_heroku


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

APPEND_SPLASH = False

SECRET_KEY = "es=-0f)*cb5=t%!+yaopldr_+r5je3si61--1^18dwrz_^(ke%"

DEBUG = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        # 'rest_framework.authentication.OAuth2Authentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        #     'oauth2_provider.ext.rest_framework.TokenHasReadWriteScope',
        #     'rest_framework.permissions.IsAdminUser',
        #     'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
    ),
}

OAUTH2_PROVIDER = {
    #     # this is the list of available scopes
    #     'OAUTH2_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
}

AUTHENTICATION_BACKENDS = (
    # если раскомментить то не работает аждминка
    'django.contrib.auth.backends.ModelBackend',
    # 'django.contrib.auth.backends.ModelBackend'  # To keep the Browsable API
    # 'oauth2_provider.backends.OAuth2Backend',
)

ALLOWED_HOSTS = ['0.0.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'oauth2_provider',
    'rest_framework',
    'cat_app',
    # 'corsheaders',
    # 'registration'
    # 'registration.apps.RegistrationConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    # 'django.contrib.auth.middleware.RemoteUserMiddleware',

    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'it_cat_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, '../it_cat_project/templates'),
            # os.path.join(PROJECT_ROOT, '../it_cat_project/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'it_cat_project.wsgi.application'
# WSGI_APPLICATION = 'wsgi.application'
# SESSION_COOKIE_NAME = 'oauth2server_sessionid'

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qgr4mak5mmbu3r5r',
        'USER': 'nuat27kb7mvpfsfd',
        'PASSWORD': 'rf8x36857whi984d',
        'HOST': 'ixqxr3ajmyapuwmi.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',

        # 'OPTIONS': {'sslmode': None},
    }

}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))
# DATABASES['default'] = dj_database_url.parse('mysql://nuat27kb7mvpfsfd:rf8x36857whi984d@ixqxr3ajmyapuwmi
# .cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/qgr4mak5mmbu3r5r', conn_max_age=600)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ALLOWED_HOSTS = ['0.0.0.0']
CORS_ORIGIN_ALLOW_ALL = True

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
# print(DATABASES)
try:
    del DATABASES['default']['OPTIONS']['sslmode']
except:
    pass
