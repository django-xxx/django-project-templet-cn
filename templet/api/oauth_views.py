# -*- coding: utf-8 -*-

from __future__ import division

from django.conf import settings
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse
from furl import furl

from utils.redis.connect import r
from utils.user.userinfo_save import userinfo_save


@transaction.atomic
def oauth_redirect(request):
    # Save profile or something else
    user = userinfo_save(request.GET)

    token_check_key = getattr(user, settings.TOKEN_CHECK_KEY)

    query_params = {
        settings.TOKEN_CHECK_KEY: token_check_key,
        'vtoken': r.token(token_check_key, ex=False, buf=False),
    }

    return redirect(furl(reverse('page:user_oauth')).add(request.GET).add(query_params).url)
