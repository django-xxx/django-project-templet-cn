# -*- coding: utf-8 -*-


def DJANGO_WE_CFG_FUNC(request, state=None):
    """ WeChat CFG Callback Func """


def DJANGO_WE_BASE_FUNC(code, state, access_info=None):
    """ WeChat Base Redirect Callback Func """


def DJANGO_WE_USERINFO_FUNC(code, state, access_info=None, userinfo=None):
    """ WeChat Userinfo Redirect Callback Func """
    from django.conf import settings
    from utils.redis.connect import r

    # Save profile or something else

    token_check_key = 'token_check_key'

    return {
        settings.TOKEN_CHECK_KEY: token_check_key,
        'vtoken': r.token(token_check_key, ex=False, buf=False),
    }
