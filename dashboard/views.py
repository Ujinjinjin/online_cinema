from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from client.models import *
from .models import *
from django.db import connection
from .string_resources import get_resources


def index(request):
    if request.user.is_authenticated and request.user.is_staff:
        resources = get_resources(request)
        return render(request, 'dashboard/index.html', context={'resources': resources.PAGE_INDEX})
    else:
        return redirect('dashboard:sign_in')


def interactive_report(request):
    return None


def sign_in(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard:index')
    else:
        resources = get_resources(request)
        if request.POST:
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)

            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('dashboard:index')
                else:
                    messages.add_message(request, messages.INFO, resources.WARNING_REQUIRED_ADMIN)  # Create message
            else:
                messages.add_message(request, messages.ERROR, resources.ERROR_INVALID_LOGIN)  # Create message
    return render(request, 'dashboard/sign_in.html', context={'resources': resources.PAGE_SIGN_IN})


def simple_report(request, table_name):
    if request.user.is_authenticated and request.user.is_staff:
        select_from = tables[table_name]['select_from']
        headers = tables[table_name]['uid']
        title = tables[table_name]['title']
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {select_from} ORDER BY id')
        rows = cursor.fetchall()
        return render(request, 'dashboard/simple_report.html', context={'title': title,
                                                                        'headers': headers,
                                                                        'table': rows,
                                                                        })
    else:
        return redirect('dashboard:sign_in')