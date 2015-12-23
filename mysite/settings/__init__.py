# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import os

__author__ = 'hjf'
from .prod import *
# if 'SERVER_SOFTWARE' in os.environ:
#     from .prod import *
# else:
#     from .dev import *
