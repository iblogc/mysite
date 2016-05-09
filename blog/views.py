# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from django.utils.decorators import method_decorator
from django.views.decorators.http import last_modified
from django.views.generic import DetailView, CreateView
from blog.forms import PostForm
from blog.models import Post
from common.views import OwerListView


def latest_post_time(request, slug):
    return Post.objects.get(slug=slug).updated_at


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

    @method_decorator(last_modified(latest_post_time))
    def get(self, request, *args, **kwargs):
        return super(PostDetail, self).get(request, *args, **kwargs)


class PostList(OwerListView):
    model = Post
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content_raw', 'author']
