# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.views.generic import DetailView, CreateView
from blog.models import Post
from common.views import OwerListView
from utils.markdown import md


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super(PostDetail, self).get_object()
        obj.content_html = md(obj.content_raw)
        print obj.content_html
        print 456789
        return obj

class PostList(OwerListView):
    model = Post
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content_raw', 'author']