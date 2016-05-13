"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings
from news.views import index as news_views_index
from news.views import column_detail as news_views_column_detail
from news.views import article_detail as news_views_article_detail

urlpatterns = [
    url(r'^$', news_views_index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', news_views_column_detail, name='column'),
    url(r'^news/(?P<article_slug>[^/]+)/$', news_views_article_detail, name='article'),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    