# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$',views.main, name='main'),
	url(r'^index/$',views.index, name='index'),
	url(r'^login/$',views.login, name='login'),
	url(r'^logout/$',views.logout, name='logout'),
	url(r'^posting/$',views.posting, name='posting'),
	url(r'^auth_pusher/$',views.auth_pusher, name='auth_pusher'),
]