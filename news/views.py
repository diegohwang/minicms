from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(u'欢迎来黄金书院学习Django')

def column_detail(request, column_slug):
    return HttpResponse('column slug: ' + column_slug)

def article_detail(requset, article_slug):
    return HttpResponse('article slug: ' + article_slug)