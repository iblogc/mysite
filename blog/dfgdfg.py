# -*- coding: utf-8 -*-
import django
from django.db.models import Count, Sum, Max, Avg

django.setup()
from blog.models import Author, Book


__author__ = 'hjf'


#
# author = Author.objects.create(name='jim', age=13)
# Book.objects.bulk_create([Book(name='java', user=author), Book(name='python',
#                                                                user=author)])
# print Author.objects.filter(bbb__name='java')
# for b in Book.objects.all():
#     print b.name
# for a in Author.objects.all():
#     print a.age
# print '+++'
# aa = Book.objects.all().annotate(Sum('user'))
# print aa[1].user__sum
# # print aa[1].age__avg
# print '+++'
# aaa = Author.objects.all().aggregate(Sum('age'), Avg('age'))
# print aaa

# print Author.objects.annotate(Count('bbb')).filter(bbb__count__gt=1)
# print Book.objects.aggregate(Count('user'))
from django.db.models import When, F, Q
print When(True, then='name')