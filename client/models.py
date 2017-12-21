#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.utils.timezone import now
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
import os


class LongCharField(models.CharField):
    """A basically unlimited-length CharField."""
    description = _("Unlimited-length string")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = int(1e9)
        super(models.CharField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'LongCharField'

    def db_type(self, connection):
        return 'nvarchar(max)'

    def formfield(self, **kwargs):
        return super(models.CharField, self).formfield(**kwargs)


class AccessLevel(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    lvl = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return f'{self.tag} ({self.lvl})'

    class Meta:
        verbose_name = _('access level')
        verbose_name_plural = _('access levels')
        db_table = '_AccessLevel'


class Member(models.Model):
    ACTOR = 'ACT'
    DIRECTOR = 'DIR'
    COMPOSER = 'COM'
    ROLE_CHOICES = (
        (ACTOR, 'Artist'),
        (DIRECTOR, 'Director'),
        (COMPOSER, 'Composer')
    )
    first_name = models.CharField(max_length=50, default='First Name')
    last_name = models.CharField(max_length=50, default='Last Name')
    portrait = models.ImageField(upload_to=f'media/members/', null=True, default=None)
    role_in_movie = models.CharField(max_length=4, choices=ROLE_CHOICES, default=ACTOR)

    def __str__(self):
        return f'{self.first_name} {self.last_name}. {self.role_in_movie}'

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
        db_table = '_Member'


class Genre(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
        db_table = '_Genre'


class Movie(models.Model):
    title = models.CharField(max_length=150)
    duration = models.IntegerField(default=0)
    movie_description = LongCharField()  # models.CharField(max_length=350)  # LongCharField()
    release_date = models.DateField()
    poster = models.FileField(upload_to='media/movies/', null=True)
    trailer_url = LongCharField()  # models.CharField(max_length=350)  # LongCharField()
    suggested = models.BooleanField(default=False)
    access_lvl = models.ForeignKey(AccessLevel, on_delete=models.SET_DEFAULT, default=0)
    # members = models.ManyToManyField(Member, db_table='_MovieMember')
    # genres = models.ManyToManyField(Genre, db_table='_MovieGenre')

    def __str__(self):
        return f'{self.title} ({self.release_date})'

    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')
        db_table = '_Movie'


class MovieMember(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.movie)} - {str(self.member)}'

    class Meta:
        verbose_name = _('movie_member')
        verbose_name_plural = _('movie_members')
        db_table = '_MovieMember'
        unique_together = ('movie', 'member')


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.movie)} - {str(self.genre)}'

    class Meta:
        verbose_name = _('movie_genre')
        verbose_name_plural = _('movie_genre')
        db_table = '_MovieGenre'
        unique_together = ('movie', 'genre')


class Image(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=f'media/images/')

    def __str__(self):
        return f'{self.file.name.replace("media/", "")}'

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        db_table = '_Image'


class Subscription(models.Model):
    duration = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    visible = models.BooleanField(default=False)
    access_level = models.ForeignKey(AccessLevel, on_delete=models.SET_DEFAULT, default=0)

    def __str__(self):
        return f'{self.access_level} - {self.price}. ({self.duration} days).'

    class Meta:
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')
        db_table = '_Subscription'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, max_length=100)
    first_name = LongCharField()  # models.CharField(max_length=350)  # LongCharField(default='First Name')
    last_name = LongCharField()  # models.CharField(max_length=350)  # LongCharField(default='Last Name')
    activated = models.BooleanField(_('activated'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False, editable=False)
    is_superuser = models.BooleanField(_('superuser'), default=False, editable=False)
    subscribed_date = models.DateField(default=now)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_DEFAULT, default=None, null=True)
    lang = models.CharField(_('language'), max_length=5, default='en-us')
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
    liked = models.BooleanField(default=False)
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
    code = models.CharField(max_length=15, unique=True)
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
