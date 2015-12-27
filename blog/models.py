# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.db import models

from common.models import TimeInfo
from uuslug import uuslug
from utils.markdown import md

___author__ = 'korvin101'


@python_2_unicode_compatible
class Category(models.Model):
    """归档表"""

    name = models.CharField(_('归档名称'), max_length=10, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = _('归档')
        verbose_name_plural = _('归档')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Category, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Tag(models.Model):
    """标签表"""

    name = models.CharField(_('标签'), max_length=10, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        db_table = 'tag'
        verbose_name = _('标签')
        verbose_name_plural = _('标签')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Tag, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Post(TimeInfo):
    """文章表"""

    title = models.CharField(_('博文标题'), max_length=30,
                             default='', help_text=_('长度在50字以内'),
                             error_messages={'max_length': _('标题太长了')}
                             )
    cover = models.ImageField(_('封面'), max_length=50, blank=True)
    content_raw = models.TextField(_('博文内容（markdown格式）'), default='')
    content_html = models.TextField(_('博文内容（html格式）'), blank=True,
                                    editable=False, default='')
    is_markdown = models.BooleanField(_('使用Markdown语法书写'), default=False,
                                      help_text=_('语法详见http://'
                                                  'www.appinn.com/markdown/'))
    category = models.ForeignKey(Category, models.SET_NULL,
                                 verbose_name=_('归档'),
                                 blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL,
                               blank=True, null=True, verbose_name=_('作者'))
    # tags = TaggableManager(_('标签'), blank=True,
    #                       help_text=_('多个标签请以英文逗号分隔'))
    tags = models.ManyToManyField(Tag, verbose_name=_('标签'), blank=True)

    allow_comment = models.BooleanField(_('允许评论'), default=True)

    class Meta:
        db_table = 'post'
        verbose_name = _('文章')
        verbose_name_plural = _('文章')
        # 一个人一个自然天内不能发相同标题的博文
        unique_together = ('title', 'created_at', 'author')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        self.content_html = md(self.content_raw)
        super(Post, self).save(*args, **kwargs)
