# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url
from blog.decorator import pjax

from blog.views import PostDetail, PostList, PostCreate

__author__ = 'korvin101'

urlpatterns = [
    url(r'^$', pjax(PostList.as_view(), 'blog/post_list_pjax.html'), name='post_list'),
    url(r'^post/$', pjax(PostList.as_view(), 'blog/post_list_pjax.html'), name='post_list'),
    url(r'^post/(?P<slug>[\w-]+)/$', pjax(PostDetail.as_view(), 'blog/post_detail_pjax.html'), name='post_detail'),
    url(r'^create/post/$', PostCreate.as_view(), name='create_post'),
]
