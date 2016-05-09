# -*- coding: utf-8 -*-
import django
from outil.markdown import md

django.setup()
from blog.models import Post
from blog.forms import PostForm

__author__ = 'korvin101'


# p = Post.objects.get(pk=1)
# print p
# print p.updated_at
# p.set_top()
# print p.updated_at

# print md("# sdfsdf")

p = Post()
pf = PostForm()
print pf