# -*- coding: utf-8 -*-

import redis_extensions as redis


def redis_conf(conf):
    return {
        'host': conf.get('HOST', 'localhost'),
        'port': conf.get('PORT', 6379),
        'password': '{0}:{1}'.format(conf.get('USER', ''), conf.get('PASSWORD', '')) if conf.get('USER') else '',
        'db': conf.get('db', 0),
    }


def redis_connect(conf):
    return redis.StrictRedisExtensions(connection_pool=redis.ConnectionPool(**redis_conf(conf)))
