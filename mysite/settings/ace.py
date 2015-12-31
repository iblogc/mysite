# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import sys

from .base import *

__author__ = 'hjf'

DEBUG = True

# sys.path.append("/home/bae/app/deps/")
sys.path.append('%s%s' % (BASE_DIR, '\\deps'))
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'rds09tgm35r28edg2y0m.mysql.rds.aliyuncs.com',
        'NAME': 'rds09tgm35r28edg2y0m',
        'USER': 'btn3wq9lrg28agwd',
        'PASSWORD': 'wYT4r6T2dYNZWpju',
        'PORT': '3306',
    }
}
LOGGING = {}
