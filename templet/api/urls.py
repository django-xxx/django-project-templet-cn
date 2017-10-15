# -*- coding: utf-8 -*-

from django.conf.urls import url

from api import oauth_views


urlpatterns = [
]

urlpatterns += [
    url(r'^3rd/or$', oauth_views.oauth_redirect, name='3rd_or'),
    url(r'^3rd/oauth_redirect$', oauth_views.oauth_redirect, name='3rd_oauth_redirect'),
]
