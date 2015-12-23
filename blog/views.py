# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.views.generic import DetailView, ListView, CreateView
from blog.models import Post
from common.views import OwerListView


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class PostList(OwerListView):
    model = Post
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content_raw', 'author']