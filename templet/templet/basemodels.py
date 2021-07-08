# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModelMixin(models.Model):
    status = models.BooleanField(_('status'), default=True, help_text=_('Status'))
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True, editable=True, help_text=_('Create Time'))
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True, editable=True, help_text=_('Update Time'))

    class Meta:
        abstract = True


class SexModelMixin(models.Model):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2

    SEX_TUPLE = (
        (UNKNOWN, '未知'),
        (MALE, '男'),
        (FEMALE, '女'),
    )

    sex = models.IntegerField(_('sex'), choices=SEX_TUPLE, default=UNKNOWN, help_text=_('Sex'))

    class Meta:
        abstract = True
