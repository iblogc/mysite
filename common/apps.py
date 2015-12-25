# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommonConfig(AppConfig):
    name = 'common'
    verbose_name = _('公用')
