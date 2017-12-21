#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RuRu:
    ERROR_INVALID_LOGIN = 'Упс. Неверная почта или пароль. Проверьте их правильность и повторите еще раз.'

    WARNING_REQUIRED_ADMIN = 'Внимание! Пожалуйста, авторизуйтесь под своим логином и паролем администратора.'
    WARNING_SOMETHING_WENT_WRONG = 'Внимание! Что-то пошло не так. Примите наши извинения и повторите еще раз.'

    PAGE_INDEX = {'button_submit': 'Подтвердить',
                  'label_file': 'Выберите файл',
                  'tab_settings': 'Настройки',
                  'tab_upload': 'Загрузить',
                  'title': 'Online Cinema | Dashboard',
                  }

    PAGE_SIGN_IN = {'button_login': 'Войти',
                    'label_email': 'Email',
                    'label_password': 'Пароль',
                    'placeholder_email': 'Введите email...',
                    'placeholder_password': 'Введите пароль...',
                    'tab_sign_in': 'Вход',
                    'title': 'Online Cinema | Вход в панель управления',
                    }

    def __str__(self):
        return 'ru-ru'


class EnUs:
    ERROR_INVALID_LOGIN = 'Oops. Email or password is not right. Please check it and try again.'

    WARNING_REQUIRED_ADMIN = 'Warning! Please log in with your admin account email and password.'
    WARNING_SOMETHING_WENT_WRONG = 'Warning! Something went wrong. Please forgive us and try again.'

    PAGE_INDEX = {'button_submit': 'Submit',
                  'label_file': 'Choose file',
                  'tab_settings': 'Settings',
                  'tab_upload': 'Upload',
                  'title': 'Online Cinema | Dashboard',
                  }

    PAGE_SIGN_IN = {'button_login': 'Login',
                    'label_email': 'Email',
                    'label_password': 'Password',
                    'placeholder_email': 'Enter email...',
                    'placeholder_password': 'Enter password...',
                    'tab_sign_in': 'Sign In',
                    'title': 'Online Cinema | Dashboard Sign In',
                    }

    def __str__(self):
        return 'en-us'


__language_codes = {
    'ru-ru': RuRu(),
    'en-us': EnUs(),
}


def get_resources(request=None):
    if request.user.is_authenticated:
        language_set = __language_codes.get(request.user.lang, 'en-us')
        return language_set
    else:
        language_set = __language_codes.get(request.session.get('lang', 'en-us'), 'en-us')
        return language_set


if __name__ == '__main__':
    res = get_resources()
    a = []
    for key, value in res.PAGE_SIGN_IN.items():
        a.append(key)
    a.sort()
    for i in a:
        print(i)
