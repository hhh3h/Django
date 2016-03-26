#!-*- encoding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # as_view()을 통해 overriding이 가능 IndexView.as_view(template_name="about.html")
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]