#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
from .models import *
from .string_resources import get_resources
from .tokens import account_activation_token, reset_password_token
from . import errors


def activate(request, uidb64, token):
    resources = get_resources(request)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print(uid)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None
        print(e)
    if user is not None and account_activation_token.check_token(user, token):
        user.activated = True
        user.save()
        login(request, user)
        messages.add_message(request, messages.SUCCESS, resources.SUCCESS_EMAIL_CONFIRMED)  # Create message
        return redirect('client:index')
    else:
        messages.add_message(request, messages.ERROR, resources.ERROR_ACTIVATION_LINK_IS_INVALID)  # Create message
        if request.user.is_authenticated:  # Разлогиниваемся на всякий случай
            logout(request)
        return redirect('client:sign_in')


def change_lang(request, lang_code):
    request.session['lang'] = lang_code
    if request.user.is_authenticated:
        request.user.lang = lang_code
        request.user.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def index(request):
    resources = get_resources(request)
    return render(request, 'client/index.html', context={'resources': resources.PAGE_INDEX})


def reset_password(request, uidb64, token):
    resources = get_resources(request)
    if request.user.is_authenticated:  # Разлогиниваемся на всякий случай
        logout(request)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if request.POST:
        try:
            password = request.POST["password"]
            errors.check_data(password=password)
            if user is not None:
                user.set_password(password)
                user.save()
                login(request, user)
                messages.add_message(request, messages.SUCCESS, resources.SUCCESS_PASSWORD_CHANGED)  # Create msg
                return redirect('client:index')
            else:
                messages.add_message(request, messages.WARNING, resources.WARNING_SOMETHING_WENT_WRONG)  # Create msg
                return redirect('client:sign_in')
        except errors.ShortPasswordError:
            messages.add_message(request, messages.ERROR, resources.ERROR_SHORT_PASSWORD)  # Create message
            return render(request, 'client/reset_password.html', context={'uid': uidb64, 'token': token})
    else:
        if user is not None and reset_password_token.check_token(user, token):
            return render(request, 'client/reset_password.html', context={'uid': uidb64, 'token': token})
        else:
            messages.add_message(request, messages.ERROR, resources.ERROR_RECOVERY_LINK_IS_INVALID)  # Create message
            return redirect('client:sign_in')


def restore(request):
    resources = get_resources(request)
    if request.user.is_authenticated:  # Разлогиниваемся на всякий случай
        logout(request)
    if request.POST:
        email = request.POST["email"]
        try:
            user = User.objects.get(email=email)
            # Create confirmation link
            current_site = get_current_site(request)
            html_message = render_to_string('client/email_pswrd_reset.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': str(urlsafe_base64_encode(force_bytes(user.pk)))[2:-1],
                'token': reset_password_token.make_token(user)
            })
            text_message = strip_tags(html_message)
            # Create and email message with confirmation link
            mail_subject = 'Password recovery'  # TODO Заменить
            email_message = EmailMultiAlternatives(mail_subject, text_message, to=[email])
            email_message.attach_alternative(html_message, "text/html")
            email_message.send()
            # Create message
            messages.add_message(request, messages.INFO, resources.INFO_RESET_PASSWORD.format(email))
            return redirect('client:sign_in')
        except User.DoesNotExist:
            messages.add_message(request, messages.ERROR, resources.ERROR_EMAIL_DOES_NOT_EXIST)
            return redirect('client:restore')
    return render(request, 'client/restore.html', context={'resources': resources.PAGE_RESTORE})


def sign_in(request):
    resources = get_resources(request)
    if not request.user.is_authenticated:
        if request.POST:
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                if not request.user.activated:  # If account not activated create message
                    messages.add_message(request, messages.INFO, resources.INFO_CONFIRM_EMAIL)  # Create message
                return redirect('client:index')
            else:
                messages.add_message(request, messages.ERROR, resources.ERROR_INVALID_LOGIN)  # Create message
        return render(request, 'client/sign_in.html', context={'resources': resources.PAGE_SIGN_IN})
    else:
        return redirect('client:index')


def sign_out(request):
    logout(request)
    return redirect('client:index')


def sign_up(request):
    resources = get_resources(request)
    if request.POST:
        try:
            email = request.POST["email"]
            password = request.POST["password"]
            errors.check_data(email, password)
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            user = User()
            user.email = email
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            # Create confirmation link
            current_site = get_current_site(request)
            html_message = render_to_string('client/email_acc_active.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': str(urlsafe_base64_encode(force_bytes(user.pk)))[2:-1],
                'token': account_activation_token.make_token(user)
            })
            text_message = strip_tags(html_message)
            # Create and email message with confirmation link
            mail_subject = 'Please activate your account'  # TODO Заменить
            email_message = EmailMultiAlternatives(mail_subject, text_message, to=[email])
            email_message.attach_alternative(html_message, "text/html")
            email_message.send()
            # Create message after registration
            messages.add_message(request, messages.INFO, resources.INFO_CONFIRM_EMAIL)  # Create message
            return redirect('client:index')
        except IntegrityError:
            messages.add_message(request, messages.ERROR, resources.ERROR_EMAIL_IS_ALREADY_USED)  # Create message
        except errors.ShortPasswordError:
            messages.add_message(request, messages.ERROR, resources.ERROR_SHORT_PASSWORD)  # Create message
        except errors.InvalidEmailError:
            messages.add_message(request, messages.ERROR, resources.ERROR_INCORRECT_EMAIL)  # Create message
        except TimeoutError:
            user.delete()
            messages.add_message(request, messages.WARNING, resources.WARNING_SOMETHING_WENT_WRONG)  # Create message
    return redirect('client:sign_in')


def movie(request, mov_id):
    return JsonResponse({"message": f"You're on the page of movie with id={mov_id}"})
