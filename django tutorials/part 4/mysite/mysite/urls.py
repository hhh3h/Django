#!-*- encoding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

# admin.site만 제외하고 app의 urls을 읽어올때는 반드시 include을 사용 한다.
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]