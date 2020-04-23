# -*- coding: utf-8 -*-

"""templet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api/', include(('api.urls', 'api'), namespace='api')),
    url(r'^uniapi/', include(('django_uniapi.urls', 'uniapi'), namespace='uniapi')),
]

urlpatterns += [
    # url(r'^s/', include(('django_short_url.urls', 'django_short_url'), namespace='django_short_url')),
]

urlpatterns += [
    url(r'^w/', include(('django_we.urls', 'shortwechat'), namespace='shortwechat')),
    url(r'^we/', include(('django_we.urls', 'wechat'), namespace='wechat')),
]

urlpatterns += [
    # url(r'^p/', include(('page.urls', 'shortpage'), namespace='shortpage')),
    # url(r'^page/', include(('page.urls', 'page'), namespace='page')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# AdminSite
admin.site.site_header = 'Django administration'
admin.site.site_title = 'Django site admin'
# Make site_url/index_title None to hidden
admin.site.site_url = '/'
admin.site.index_title = 'Site administration'
