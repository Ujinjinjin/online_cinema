#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
import os


class LongCharField(models.CharField):
    "A basically unlimited-length CharField."
    description = _("Unlimited-length string")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = int(1e9)
        super(models.CharField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'LongCharField'

    def db_type(self, connection):
        return 'varchar(max)'

    def formfield(self, **kwargs):
        return super(models.CharField, self).formfield(**kwargs)


class Member(models.Model):
    ARTIST = 'ART'
    DIRECTOR = 'DIR'
    ROLE_CHOICES = (
        (ARTIST, 'Artist'),
        (DIRECTOR, 'Director')
    )
    first_name = LongCharField(default='First Name')
    last_name = LongCharField(default='Last Name')
    portrait = models.ImageField(upload_to=f'media/members/{str(first_name)[0]}', null=True, default=None)
    role = models.CharField(max_length=4, choices=ROLE_CHOICES, default=ARTIST)

    def __str__(self):
        return f'{self.first_name} {self.last_name}. {self.role}'

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        db_table = '_Member'


class Genre(models.Model):
    tag = LongCharField()

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
        db_table = '_Genre'


class Movie(models.Model):
    FREE = 'FREE'
    SILVER = 'SLVR'
    GOLD = 'GOLD'
    PLATINUM = 'PLTN'
    ACCESS_LVL_CHOICES = (
        (FREE, 'Free'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum')
    )
    name = LongCharField()
    duration = models.IntegerField(default=0)
    description = LongCharField()
    release_date = models.DateField()
    poster = models.FileField(upload_to=f'media/movies/{str(name)} ({str(release_date)})')
    trailer_url = LongCharField()
    required_al = models.CharField(max_length=4, choices=ACCESS_LVL_CHOICES)
    members = models.ManyToManyField(Member, null=True, default=None, db_table='_MovieMembers')
    genres = models.ManyToManyField(Genre, null=True, default=None, db_table='_MovieGenres')
    suggested = models.BooleanField(default=False)
    # rating = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name} ({self.release_date})'

    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')
        db_table = '_Movie'


class Image(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=f'media/movies/{str(movie)})/images')

    def __str__(self):
        return f'{self.file.name.replace("media/", "")}'

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        db_table = '_Image'


class Subscription(models.Model):
    FREE = 'FREE'
    SILVER = 'SLVR'
    GOLD = 'GOLD'
    PLATINUM = 'PLTN'
    ACCESS_LVL_CHOICES = (
        (FREE, 'Free'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum')
    )
    duration = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    access_level = models.CharField(max_length=4, choices=ACCESS_LVL_CHOICES)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.access_level} - {self.price}. ({self.duration} days).'

    class Meta:
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')
        db_table = '_Subscription'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = LongCharField(default='First Name')
    last_name = LongCharField(default='Last Name')
    subscribed_date = models.DateField(default=datetime.today())
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_DEFAULT, default=None)
    activated = models.BooleanField(_('activated'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False, editable=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = '_User'

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class MovieCard(models.Model):
    watched = models.BooleanField(default=False)
    want_to_watch = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    personal_rating = models.SmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.movie}'

    class Meta:
        verbose_name = _('movie card')
        verbose_name_plural = _('movie cards')
        db_table = '_MovieCard'
        unique_together = (('user', 'movie'),)


class PromoCode(models.Model):
    code = models.CharField(max_length=15)
    quantity = models.IntegerField(default=0)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} - {self.subscription}'

    class Meta:
        verbose_name = _('promo code')
        verbose_name_plural = _('promo codes')
        db_table = '_PromoCode'


class UserPromoCode(models.Model):
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} ||| {self.promo_code.code}'

    class Meta:
        verbose_name = _("user's promo code")
        verbose_name_plural = _("user's promo codes")
        db_table = '_UserPromoCode'
        unique_together = (('user', 'promo_code'),)
