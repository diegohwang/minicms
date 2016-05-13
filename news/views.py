#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Column, Article

# Create your views here.

def index(request):
    #return HttpResponse(u'欢迎来黄金书院学习Django')
    columns = Column.objects.all()
    return render(request, 'index.html', {'columns': columns})

def column_detail(request, column_slug):
    #return HttpResponse('column slug: ' + column_slug)
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})

def article_detail(requset, article_slug):
    #return HttpResponse('article slug: ' + article_slug)
    article = Article.objects.get(slug=article_slug)
    return render(request, 'news/article.html', {'article': article})