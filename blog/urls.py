# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url

from blog.views import PostDetail, PostList, PostCreate

__author__ = 'korvin101'

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^post/$', PostList.as_view(), name='post_list'),
    url(r'^post/(?P<slug>[\w-]+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^create/post/$', PostCreate.as_view(), name='create_post'),
]
