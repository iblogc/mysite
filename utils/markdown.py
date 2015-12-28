# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import markdown
from markdown.extensions import codehilite
from markdown.extensions.codehilite import CodeHilite

__author__ = 'hjf'

def md(text):
    return markdown.markdown(text, extensions=['codehilite',
                                               'pymdownx.superfences',
                                               'tables'], extension_configs={
        'codehilite': {'linenums': False}})
