#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(AccessLevel)
admin.site.register(Member)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieMember)
admin.site.register(MovieGenre)
admin.site.register(Image)
admin.site.register(Subscription)
admin.site.register(User)
admin.site.register(MovieCard)
admin.site.register(PromoCode)
admin.site.register(UserPromoCode)
