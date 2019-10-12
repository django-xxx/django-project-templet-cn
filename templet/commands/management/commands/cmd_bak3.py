# -*- coding: utf-8 -*-

import logging

from django.db import transaction
from django_six import CompatibilityBaseCommand, close_old_connections


logger = logging.getLogger('console')


class Command(CompatibilityBaseCommand):
    def handle(self, *args, **options):
        # Crontab
        # 5 0 * * * /home/../python /home/../manage.py cmd_bak3

        logger.info('Templet bak cmd is dealing')

        close_old_connections()

        with transaction.atomic():
            pass

        close_old_connections()
