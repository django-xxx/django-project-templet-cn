# -*- coding: utf-8 -*-

from functools import wraps

from django.conf import settings
from django.shortcuts import redirect
from furl import furl
from pywe_oauth import get_oauth_redirect_url
from pywe_sign import check_signature

from utils.error.errno_utils import SignatureStatusCode
from utils.error.response_utils import response
from utils.redis.connect import r


def check_user_cookie(func=None, key=settings.COOKIE_USER_CHECK_KEY):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(request, *args, **kwargs):
            user_id = request.get_signed_cookie(key, default='', salt=settings.COOKIE_SALT)
            if not user_id:
                return redirect(get_oauth_redirect_url(settings.WECHAT_OAUTH2_REDIRECT_URI, 'snsapi_userinfo', request.get_full_path()))
            return func(request, *args, **kwargs)
        return returned_wrapper

    if not func:
        def foo(func):
            return decorator(func)
        return foo

    return decorator(func)


def check_token(func=None, entry=None):
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
                    redirect_url = furl(entry or settings.WECHAT_OAUTH2_REDIRECT_ENTRY).add({}).url
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
                return response(SignatureStatusCode.SIGNATURE_ERROR)
            return func(request, *args, **kwargs)
        return returned_wrapper

    if not func:
        def foo(func):
            return decorator(func)
        return foo

    return decorator(func)


def check_cookie(func=None, entry=None):
    def decorator(func):
        @wraps(func)
        def returned_wrapper(request, *args, **kwargs):
            if not settings.DEBUG and not request.COOKIES.get('user_id'):
                # 3rd OAuth
                # return redirect(settings.WECHAT_OAUTH2_REDIRECT_URL)
                # Current OAuth
                redirect_url = furl(entry or settings.WECHAT_OAUTH2_REDIRECT_ENTRY).add({}).url
                return redirect(get_oauth_redirect_url(settings.WECHAT_OAUTH2_REDIRECT_URI, 'snsapi_userinfo', redirect_url))
            return func(request, *args, **kwargs)
        return returned_wrapper

    if not func:
        def foo(func):
            return decorator(func)
        return foo

    return decorator(func)
