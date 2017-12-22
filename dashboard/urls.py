#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
# from django.urls import path, re_path
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^interactive_report/(?P<table_name>[A-Za-z_ ]+)/?$', views.interactive_report, name='interactive_report'),
    url(r'^report_with_form/(?P<table_name>[A-Za-z_ ]+)/?$', views.report_with_form, name='report_with_form'),
    url(r'^sign_in/?$', views.sign_in, name='sign_in'),
    url(r'^simple_report/(?P<table_name>[A-Za-z_ ]+)/?$', views.simple_report, name='simple_report'),
    # url(r'^sign_in/?$', views.sign_in, name='sign_in'),
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
