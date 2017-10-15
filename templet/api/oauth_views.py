# -*- coding: utf-8 -*-

from __future__ import division

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import redirect
from furl import furl

from utils.redis.connect import r


@transaction.atomic
def oauth_redirect(request):
    # Save profile or something else
    unique_identifier = request.GET.get(settings.WECHAT_UNIQUE_IDENTIFICATION, '')

    token_check_key = 'token_check_key'

    query_params = {
        settings.TOKEN_CHECK_KEY: token_check_key,
        'vtoken': r.token(token_check_key, ex=False, buf=False),
    }

    return redirect(furl(reverse('page:user_oauth')).add(request.GET).add(query_params).url)
