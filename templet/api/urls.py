# -*- coding: utf-8 -*-

from django.urls import re_path

from api import oauth_views


urlpatterns = [
]

urlpatterns += [
    re_path(r'^3rd/or$', oauth_views.oauth_redirect, name='3rd_or'),
    re_path(r'^3rd/oauth_redirect$', oauth_views.oauth_redirect, name='3rd_oauth_redirect'),
]
