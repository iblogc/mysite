# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import os
import sys

__author__ = 'hjf'
reload(sys)
sys.setdefaultencoding("utf-8")

if 'SERVER_SOFTWARE' in os.environ:
    from .bae import *
else:
    from .dev import *
