# -*- coding: utf-8 -*-

from functools import wraps

from django.conf import settings
from django.shortcuts import redirect
from furl import furl
from pywe_sign import check_signature
from pywe_oauth import get_oauth_redirect_url

from utils.redis.connect import r


def check_token(func=None):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(request, *args, **kwargs):
            if not settings.DEBUG and request.wechat:
                vtoken = request.GET.get('vtoken', '') or request.POST.get('vtoken', '')
                token_check_key = request.GET.get(settings.TOKEN_CHECK_KEY, '') or request.POST.get(settings.TOKEN_CHECK_KEY, '')
                if not r.token_exists(token_check_key, vtoken):
                    # 3rd OAuth
                    # return redirect(settings.WECHAT_OAUTH2_REDIRECT_URL)
                    # Current OAuth
                    redirect_url = furl(settings.WECHAT_OAUTH2_REDIRECT_ENTRY).add({}).url
                    return redirect(get_oauth_redirect_url(settings.WECHAT_OAUTH2_REDIRECT_URI, 'snsapi_userinfo', redirect_url))
            return func(request, *args, **kwargs)
        return returned_wrapper

    if not func:
        def foo(func):
            return decorator(func)
        return foo

    return decorator(func)


def check_sign(func=None, method='POST'):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(request, *args, **kwargs):
            if not settings.DEBUG and not check_signature(getattr(request, method).dict(), settings.PARAMS_SIGN_KEY):
                return json_response(SignatureStatusCode.SIGNATURE_ERROR)
            return func(request, *args, **kwargs)
        return returned_wrapper

    if not func:
        def foo(func):
            return decorator(func)
        return foo

    return decorator(func)
