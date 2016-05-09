# -*- coding: utf-8 -*-
from __future__ import absolute_import
import markdown

__author__ = 'hjf'


def md(text):
    return markdown.markdown(text, extensions=['codehilite', 'tables', 'toc',
                                               'pymdownx.superfences', 'nl2br',
                                               'wikilinks', 'footnotes',
                                               'abbr', 'sane_lists',
                                               'admonition', 'def_list',
                                               'attr_list'],
                             extension_configs={
                                 'codehilite': {'linenums': False}})
