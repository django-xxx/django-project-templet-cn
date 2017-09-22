# -*- coding: utf-8 -*-

# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'templet']

# DOMAIN
DOMAIN = 'http://a.com'

# 邮件设置
# 只有当 DEBUG = False 的时候，才会邮件发送报错信息
SERVER_EMAIL = 'error.notify@exmail.com'
EMAIL_HOST_USER = 'error.notify@exmail.com'
EMAIL_HOST_PASSWORD = '<^_^>pwd<^_^>'
DEFAULT_FROM_EMAIL = 'error.notify <error.notify@exmail.com>'
ADMINS = [('Zhang San', 'san.zhang@exmail.com'), ('Li Si', 'si.li@exmail.com')]
EMAIL_SUBJECT_PREFIX = u'[Templet] '
