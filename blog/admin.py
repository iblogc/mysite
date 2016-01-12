# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin
from django.utils.translation import ugettext as _
from blog.forms import PostForm

from blog.models import Post, Tag
from blog.models import Category


@admin.register(Category, Tag)
class TCAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    exclude = ['tags']
    list_display = ('title', 'category', 'author', 'created_at', 'updated_at')
    readonly_fields = ('author', 'created_at', 'updated_at', 'tags')
    # fields = (('title', 'category'), 'author')
    # filter_horizontal = ('tags',)
    fieldsets = (
        (None, {
            'fields': (
                'title', 'cover', 'content_raw', 'is_markdown', 'category',
                'tags', 'tags_str')
        }),
        (_('高级选项'), {
            # 'description': _('说明'),
            'classes': ('collapse', 'wide'),
            'fields': ('allow_comment',)
        }),
        (None, {
            'fields': (
                'author', 'created_at', 'updated_at'
            )
        })
    )

    def save_model(self, request, obj, form, change):
        obj.save()
        # 文章作者为当前编辑用户，先于Model里的save执行
        tags = form.cleaned_data['tags_str']
        for name in tags:
            obj.tags.add(Tag.objects.get_or_create(name=name)[0])
        obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
