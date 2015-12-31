# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext as _
from django import template

import logging

register = template.Library()

logger = logging.getLogger(__name__)

__author__ = 'hjf'


@register.filter
def splite_tag(queryset):
    tags_str = ''
    l = len(queryset)
    for tag in queryset:
        tag_name = '#{}# '.format(tag.name)
        tags_str = '{}{}'.format(tags_str, tag_name)
    return tags_str.rstrip()


@register.inclusion_tag('blog/tag.txt')
def generate_tag(tags):
    """传入tag对象的数组，输入带#号和链接的字符串"""
    return {'tags': tags}


@register.assignment_tag(takes_context=True)
def a(context, y):
    print context
    print y
    return y
