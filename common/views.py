# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext as _

import logging
from django.views.generic import ListView

logger = logging.getLogger(__name__)

__author__ = 'hjf'


class OwerListView(ListView):
    paginate_by = 15
