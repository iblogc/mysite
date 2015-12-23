# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import sys

from .base import *

__author__ = 'hjf'

DEBUG = False
# sys.path.append('%s%s' % (BASE_DIR, '\\extra_apps'))
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'sqld.duapp.com',
        'NAME': 'jNLPmQSqASqkpIqXUldz',
        'USER': '6037271862624b19a6c3b39f4b8d5679',
        'PASSWORD': '77da48be7e63418a97737723aa41487e',
        'PORT': '4050',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '3306',
    }
}
'''
LOGGING = {}
