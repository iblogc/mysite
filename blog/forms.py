# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.core.checks import Tags

from django.utils.translation import ugettext as _
from django import forms

import logging
from blog.models import Post, Tag

logger = logging.getLogger(__name__)

__author__ = 'hjf'


class PostForm(forms.ModelForm):
    tags_str = forms.CharField(label=_('标签'), max_length=100)

    class Meta:
        model = Post
        exclude = ['tags']

    def clean_tags_str(self):
        tags = self.cleaned_data.get('tags_str')
        if tags:
            return filter(lambda tag: tag.strip(), tags.split(','))
        return ''
