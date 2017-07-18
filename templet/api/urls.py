# -*- coding: utf-8 -*-

from django.conf.urls import url

from api import views as api_views


# 测试方式：取消注释，请求接口
urlpatterns = [
    # url(r'^test$', api_views.mail_error_test, name='mail_error_test'),  # 邮件发送错误信息测试接口
]
