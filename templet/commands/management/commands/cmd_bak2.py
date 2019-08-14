# -*- coding: utf-8 -*-

import logging

from django.db import transaction
from django_six import CompatibilityBaseCommand, close_old_connections

from utils.redis.connect import r


logger = logging.getLogger('console')


class Command(CompatibilityBaseCommand):
    def handle(self, *args, **options):

        logger.info('Templet bak cmd is dealing')

        while True:
            # r.rpush('TEMPLET_CMD_KEY', '')
            # kv = r.blpop('TEMPLET_CMD_KEY', 60)
            # k, v = (kv[0], kv[1]) if kv else (None, None)
            #
            # r.rpushjson('TEMPLET_CMD_KEY', {})
            k, v = r.blpopjson(['TEMPLET_CMD_KEY1', 'TEMPLET_CMD_KEY2'], 60)

            if not v:
                continue

            logger.info(v)

            close_old_connections()

            if k == 'TEMPLET_CMD_KEY1':
                with transaction.atomic():
                    pass

            elif k == 'TEMPLET_CMD_KEY2':
                with transaction.atomic():
                    pass

            else:
                continue

            close_old_connections()
