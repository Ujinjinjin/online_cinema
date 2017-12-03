#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return JsonResponse({'message': "You're on the main page"})


def movies(request, identificator):
    return JsonResponse({"message": f"You're on the page of movie with id={identificator}"})
