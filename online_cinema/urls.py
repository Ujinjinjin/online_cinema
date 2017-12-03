#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'^', include('client.urls')),
]
