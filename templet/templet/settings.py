# -*- coding: utf-8 -*-

"""
Django settings for templet project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0=hpv21&am(7(k5ab!^zjvvl=ntj)^i@7)87t47uzumt_5rq$+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django_short_url',
    'django_uniapi',
    'django_we',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'detect.middleware.UserAgentDetectionMiddleware',
]

ROOT_URLCONF = 'templet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

WSGI_APPLICATION = 'templet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'templet',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 600,
        'OPTIONS': {
            # Utf8mb4 for Emoji
            #
            # Nickname
            #
            # account.WechatInfo ==> nickname
            #   ALTER TABLE account_wechatinfo MODIFY COLUMN nickname VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
            'charset': 'utf8mb4',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJ_DIR, 'static').replace('\\', '/'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static').replace('\\', '/')

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

MEDIA_URL = '/media/'

# File 设置
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # InMemoryUploadedFile 文件最大值，设置为 5 MB
FILE_UPLOAD_PERMISSIONS = 0o644  # TemporaryUploadedFile 文件权限设置

# DOMAIN
DOMAIN = 'http://a.com'

# Redis 设置
REDIS = {
    'default': {
        'HOST': '127.0.0.1',
        'PORT': 6379,
        'USER': '',
        'PASSWORD': '',
        'db': 0,
    }
}

# 微信设置
WECHAT = {
    'JSAPI': {
        'token': '5201314',
        'appID': '',
        'appsecret': '',
        'mchID': '',
        'apiKey': '',
        'mch_cert': '',
        'mch_key': '',
        'redpack': {

        }
    },
}

# 微信唯一标识
# Choices: 'unionid' or 'openid'
#
# models.py
#   'unique_identifier': self.unionid if settings.WECHAT_UNIQUE_IDENTIFICATION == 'unionid' else self.openid,
# views.py
#   unique_identifier = request.POST.get(settings.WECHAT_UNIQUE_IDENTIFICATION, '')
#   profile = Profile.objects.get(**{settings.WECHAT_UNIQUE_IDENTIFICATION: unique_identifier})
WECHAT_UNIQUE_IDENTIFICATION = 'unionid'

# Token 错误重授权设置
TOKEN_CHECK_KEY = ''
# TOKEN_CHECK_KEY = 'user_id'
WECHAT_OAUTH2_REDIRECT_ENTRY = ''
WECHAT_OAUTH2_REDIRECT_URL = ''

# 邮件设置
# https://docs.djangoproject.com/en/1.11/howto/error-reporting/#email-reports
# When DEBUG is False, Django will email the users listed in the ADMINS setting
# whenever your code raises an unhandled exception and results in an internal server error (HTTP status code 500).
# 只有当 DEBUG = False 的时候，才会邮件发送报错信息
# Email address that error messages come from.
SERVER_EMAIL = 'error.notify@exmail.com'
# The email backend to use. For possible shortcuts see django.core.mail.
# The default is to use the SMTP backend.
# Third-party backends can be specified by providing a Python path
# to a module that defines an EmailBackend class.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Host for sending email.
EMAIL_HOST = 'smtp.exmail.qq.com'
# Port for sending email.
EMAIL_PORT = 25
# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'error.notify@exmail.com'
EMAIL_HOST_PASSWORD = '<^_^>pwd<^_^>'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None
# Default email address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = 'error.notify <error.notify@exmail.com>'
# People who get code error notifications.
# In the format [('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com')]
ADMINS = [('Zhang San', 'san.zhang@exmail.com'), ('Li Si', 'si.li@exmail.com')]
# Not-necessarily-technical managers of the site. They get broken link
# notifications and other various emails.
MANAGERS = ADMINS
# Subject-line prefix for email messages send with django.core.mail.mail_admins
# or ...mail_managers.  Make sure to include the trailing space.
EMAIL_SUBJECT_PREFIX = u'[Templet] '

# Admin Settings
DISABLE_ACTION = False

# 开发调试相关配置
if DEBUG:
    try:
        from local_settings_dev import *
    except ImportError:
        pass

try:
    from local_settings import *
except ImportError:
    pass

try:
    from oauth_settings import *
except ImportError:
    pass

# 依赖 local_settings 中的配置
# 微信授权设置
# WECHAT_OAUTH2_REDIRECT_URI = '{0}/we/oauth2?scope={{0}}&redirect_url={{1}}'.format(DOMAIN)
# Shorten URL
# ``o`` is short for oauth2
# ``r`` is short for redirect_url
WECHAT_OAUTH2_REDIRECT_URI = '{0}/we/o?scope={{0}}&r={{1}}'.format(DOMAIN)
WECHAT_OAUTH2_USERINFO_REDIRECT_URI = '{0}/we/o?r={{0}}'.format(DOMAIN)  # Scope default snsapi_userinfo
WECHAT_BASE_REDIRECT_URI = '{0}/we/base_redirect'.format(DOMAIN)
WECHAT_USERINFO_REDIRECT_URI = '{0}/we/userinfo_redirect'.format(DOMAIN)
WECHAT_DIRECT_BASE_REDIRECT_URI = '{0}/we/direct_base_redirect'.format(DOMAIN)
WECHAT_DIRECT_USERINFO_REDIRECT_URI = '{0}/we/direct_userinfo_redirect'.format(DOMAIN)

try:
    from func_settings import redis_connect
    REDIS_CACHE = redis_connect(REDIS.get('default', {}))
except ImportError:
    REDIS_CACHE = None

# LOGGER 设置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'console': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
