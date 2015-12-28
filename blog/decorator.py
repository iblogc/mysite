# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
import functools

__author__ = 'korvin101'


def pjax(func=None, pjax_template=None):
    def func_wrapper(func):
        @functools.wraps(func)
        def return_wrapper(request, *args, **kwargs):
            resp = func(request, *args, **kwargs)
            if 'HTTP_X_PJAX' in request.META:
                resp.template_name = pjax_template
                print 111
                print pjax_template
            print 222
            return resp
        return return_wrapper

    if func:
        return func_wrapper(func)
    else:
        return func_wrapper
