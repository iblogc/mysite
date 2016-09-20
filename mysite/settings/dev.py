# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext as _

from .base import *

__author__ = 'hjf'

DEBUG = True

STATIC_ROOT = ''
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mysite',
#         'USER': 'root',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# 本地内存缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }

# 虚拟的缓存，开发时用，不会产生缓存效果
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += ('debug_toolbar',)

# MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
#
# DEBUG_TOOLBAR_PATCH_SETTINGS = False
#
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]
#
DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL':'//cdn.bootcss.com/jquery/2.1.4/jquery.min.js'}

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
        #             'class': 'django.outil.log.AdminEmailHandler',
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
