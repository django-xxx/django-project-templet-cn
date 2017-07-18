# -*- coding: utf-8 -*-

import os


# DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

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
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

# 邮件设置
# 只有当 DEBUG = False 的时候，才会邮件发送报错信息
SERVER_EMAIL = 'error.notify@exmail.com'
EMAIL_HOST_USER = 'error.notify@exmail.com'
EMAIL_HOST_PASSWORD = '<^_^>pwd<^_^>'
DEFAULT_FROM_EMAIL = 'error.notify <error.notify@exmail.com>'
ADMINS = [('Zhang San', 'san.zhang@exmail.com'), ('Li Si', 'si.li@exmail.com')]
EMAIL_SUBJECT_PREFIX = u'[Templet] '
