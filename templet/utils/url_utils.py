# -*- coding: utf-8 -*-

from django.conf import settings


def upload_file_url(file_path):
    return file_path and ('{0}{1}'.format(settings.DOMAIN, file_path.url)) or ''
