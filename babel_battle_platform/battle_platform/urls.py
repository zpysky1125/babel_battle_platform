# coding:utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^script_upload/$', views.script_upload, name='script_upload'),
    url(r'^download/([A-Za-z0-9_.\/\-]+)/$', views.download, name='download'),
    url(r'^play/([0-9_.]+)/$', views.video_play, name='video_play'),
]