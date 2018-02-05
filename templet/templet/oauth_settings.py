# -*- coding: utf-8 -*-


def DJANGO_WE_CFG_FUNC(request, state=None):
    """ WeChat CFG Callback Func """


def DJANGO_WE_QUOTE_STATE_FUNC(request, state):
    """ WeChat Quote Callback Func """
    from utils.redis.connect import r
    return r.quote(state, short_uuid=True)


def DJANGO_WE_UNQUOTE_STATE_FUNC(request, state):
    """ WeChat UnQuote Callback Func """
    from utils.redis.connect import r
    # If Not Buf, When Wechat Multi Request, Unquote Will Get None
    # Then Once Should ReOAuth, Will Raise Error
    return r.unquote(state, buf=True) or state


def DJANGO_WE_BASE_FUNC(code, state, access_info=None):
    """ WeChat Base Redirect Callback Func """


def DJANGO_WE_USERINFO_FUNC(code, state, access_info=None, userinfo=None):
    """ WeChat Userinfo Redirect Callback Func """
    from django.conf import settings
    from utils.redis.connect import r
    from utils.user.userinfo_save import userinfo_save

    # Save profile or something else
    user = userinfo_save(userinfo)

    token_check_key = getattr(user, settings.TOKEN_CHECK_KEY)

    return {
        settings.TOKEN_CHECK_KEY: token_check_key,
        'vtoken': r.token(token_check_key, ex=True, time=r.REDIS_EXPIRED_ONE_DAY, buf=False, short_uuid=True),
    }


def DJANGO_WE_SHARE_FUNC(request, state=None):
    """ WeChat Share Callback Func """
    # from django.conf import settings
    # return settings.WECHAT_OAUTH2_REDIRECT_URL
