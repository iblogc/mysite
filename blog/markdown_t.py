# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext as _

import logging
import markdown
from markdown.extensions.codehilite import CodeHilite

logger = logging.getLogger(__name__)

__author__ = 'hjf'
a = """
```python
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content_raw', 'author']
```
"""

m = markdown.markdown(a,extensions=['codehilite','fenced_code'])
print m