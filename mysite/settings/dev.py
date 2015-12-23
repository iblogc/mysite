# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext as _

from .base import *

__author__ = 'hjf'

DEBUG = True
STATIC_ROOT = ''
# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        #         'mail_admins': {
        #             'level': 'ERROR',
        #             'class': 'django.utils.log.AdminEmailHandler',
        #             'include_html': True,
        #         },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志输出文件
            'filename': os.path.join(BASE_DIR + '/logs/',
                                     'all.log'),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 100,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR + '/logs/',
                                     'error.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 100,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR + '/logs/',
                                     'request.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 100,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR + '/logs/', 'script.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 100,
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['scprits_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['request_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'scripts': {
            'handlers': ['scprits_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'parking': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',  # 正式环境修改为INFO
            'propagate': False,
        },
    }
}
