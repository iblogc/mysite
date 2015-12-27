# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from pygments.formatters.html import HtmlFormatter
import misaka as m
from pygments import highlight
from pygments.lexers import get_lexer_by_name

__author__ = 'hjf'


class HighlighterRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        if not lang:
            return '\n<pre><code>{}</code></pre>\n'.format(
                text.strip())

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()

        return highlight(text, lexer, formatter)


renderer = HighlighterRenderer()
# renderer = HighlighterRenderer()
md = m.Markdown(renderer, extensions=('fenced-code', 'tables', 'footnotes',
                                      'autolink', 'strikethrough', 'underline',
                                      'quote', 'superscript', 'math',
                                      'highlight'))
