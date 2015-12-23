# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import sys

from .base import *

__author__ = 'hjf'

DEBUG = True

sys.path.append("/home/bae/app/deps/")

STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'sqld.duapp.com',
        'NAME': 'knPZBhcSkBsgzQanRlsU',
        'USER': 'CDa87592bf3fb11696292e89e5838180',
        'PASSWORD': '7305205bbdc097fd795909621b45051e',
        'PORT': '4050',
    }
}
LOGGING = {}
