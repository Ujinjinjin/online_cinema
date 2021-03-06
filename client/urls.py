#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
# from django.urls import path, re_path
from . import views

app_name = 'client'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^activate&(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/?$', views.activate, name='activate'),
    url(r'^change_lang&lang=(?P<lang_code>[a-zA-Z]{2}-[a-zA-Z]{2})/?$', views.change_lang, name='change_lang'),
    url(r'^movie/(?P<mov_id>\d+)/?$', views.movie, name='movie'),
    url(r'^reset_password&(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,30})/?$', views.reset_password, name='reset_password'),
    url(r'^restore/?$', views.restore, name='restore'),
    url(r'^sign_in/?$', views.sign_in, name='sign_in'),
    url(r'^sign_out/?$', views.sign_out, name='sign_out'),
    url(r'^sign_up/?$', views.sign_up, name='sign_up'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     re_path(r'activate&(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
#     path('change_lang/<str:lang_code>/', views.change_lang, name='change_lang'),
#     path('movie/<int:mov_id>/', views.movie, name='movie'),
#     re_path(r'reset_password&(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,30})/', views.reset_password, name='reset_password'),
#     path('restore/', views.restore, name='restore'),
#     path('sign_in/', views.sign_in, name='sign_in'),
#     path('sign_out/', views.sign_out, name='sign_out'),
#     path('sign_up/', views.sign_up, name='sign_up'),
# ]
