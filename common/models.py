# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models

from django.utils.translation import ugettext_lazy as _

import logging

logger = logging.getLogger(__name__)

__author__ = 'korvin101'


class TimeInfo(models.Model):
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        abstract = True


# class UserInfo(models.Model):
#     user = models.ForeignKey(User, models.SET_NULL, verbose_name='用户',
#                              blank=True, null=True)
#
#     class Meta:
#         abstract = True
