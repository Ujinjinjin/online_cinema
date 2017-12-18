#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RuRu:
    INFO_CONFIRM_EMAIL = 'Еще один шаг. Пожалуйста кликните по ссылке в сообщение на вашей почте, чтоб подтвердить почту.'
    INFO_RESET_PASSWORD = 'Еще один шаг. На почту {} была отправлена ссылка для восстановления пароля.'

    ERROR_ACTIVATION_LINK_IS_INVALID = 'Упс. Ссылка активации недействительна. Проверьте ее правильность и повторите еще раз.'
    ERROR_CONFIRM_EMAIL = 'Упс. Пожалуйста, подтвердите вашу почту перед загрузкой файла.'
    ERROR_EMAIL_DOES_NOT_EXIST = 'Упс. Аккаунта с такой почтой не существует. Проверьте правильность введенных данных и повторите еще раз.'
    ERROR_EMAIL_IS_ALREADY_USED = 'Упс. Эта почта уже исползуется. Попробуйте ввести другую.'
    ERROR_HAVE_ACTIVATED_PROMO = 'Упс. Вы уже используете промо код. Потратьте его и попробуйте еще раз.'
    ERROR_INCORRECT_EMAIL = 'Упс. Введена некоректная почта. Пожалуйста, проверьте ее и попробуйте еще раз.'
    ERROR_INVALID_LOGIN = 'Упс. Неверная почта или пароль. Проверьте их правильность и повторите еще раз.'
    ERROR_INVALID_PROMO = 'Упс. Указан неверный промокод. Проверьте его правильность и повторите еще раз.'
    ERROR_PROMO_ALREADY_USED = 'Упс. Вы уже использовали этот промо код.'
    ERROR_RECOVERY_LINK_IS_INVALID = 'Упс. Ссылка для восстановления пароля недействительна. Проверьте ее правильность и повторите еще раз.'
    ERROR_SHORT_PASSWORD = 'Упс. Длина пароля должна быть не менее 8 символов.'

    SUCCESS_CREDITS_PROMO_ACTIVATED = 'Великолепно! Промокод {} активирован. На ваш счет зачислено {} кредитов.'
    SUCCESS_DISCOUNT_PROMO_ACTIVATED = 'Великолепно! Промокод {} активирован. Вы получаете скидку {}%.'
    SUCCESS_EMAIL_CONFIRMED = 'Великолепно! Ваша почта успешно подтверждена!'
    SUCCESS_PASSWORD_CHANGED = 'Великолепно! Ваш пароль успешно изменен!'

    WARNING_SOMETHING_WENT_WRONG = 'Внимание! Что-то пошло не так. Примите наши извинения и повторите еще раз.'

    PAGE_INDEX = {'button_submit': 'Подтвердить',
                  'label_file': 'Выберите файл',
                  'tab_settings': 'Настройки',
                  'tab_upload': 'Загрузить',
                  'title': 'Online Cinema | Главная',
                  }

    PAGE_RESET_PASSWORD = {'button_submit': 'Подтвердить',
                           'label_password': 'Пароль',
                           'placeholder_password': 'Введите новый пароль...',
                           'tab_restore': 'Восстановление пароля',
                           'title': 'Online Cinema | Восстановление пароля'
                           }

    PAGE_RESTORE = {'button_submit': 'Подтвердить',
                    'label_email': 'Email',
                    'placeholder_email': 'Введите email, использованный при регистрации...',
                    'tab_restore': 'Восстановление пароля',
                    'title': 'Online Cinema | Восстановление пароля'
                    }

    PAGE_SIGN_IN = {'button_login': 'Войти',
                    'button_register': 'Зарегистрироваться',
                    'label_email': 'Email',
                    'label_first_name': 'Имя',
                    'label_last_name': 'Фамилия',
                    'label_password': 'Пароль',
                    'link_recovery_password': 'Забыли пароль?',
                    'placeholder_email': 'Введите email...',
                    'placeholder_first_name': 'Введите Ваше имя...',
                    'placeholder_last_name': 'Введите Вашу фамилию...',
                    'placeholder_password': 'Введите пароль...',
                    'tab_sign_in': 'Вход',
                    'tab_sign_up': 'Регистрация',
                    'title': 'Online Cinema | Вход',
                    }

    def __str__(self):
        return 'ru-ru'


class EnUs:
    INFO_CONFIRM_EMAIL = 'One more step. Please check your mail-box to confirm your email by clicking on the link in message.'
    INFO_RESET_PASSWORD = 'One more step. Recovery link was sent to the {} mail-box'

    ERROR_ACTIVATION_LINK_IS_INVALID = 'Oops. This activation link is invalid. Please check it and try again.'
    ERROR_CONFIRM_EMAIL = 'Oops. Please confirm your email before uploading files.'
    ERROR_EMAIL_DOES_NOT_EXIST = 'Oops. Account with this email does not exist. Please check it and try again.'
    ERROR_EMAIL_IS_ALREADY_USED = 'Oops. This email is already used. Please try another one.'
    ERROR_HAVE_ACTIVATED_PROMO = 'Oops. You can have only one activated promo in time. Use it and try again.'
    ERROR_INCORRECT_EMAIL = 'Oops. Incorrect email. Please check it and try again.'
    ERROR_INVALID_LOGIN = 'Oops. Email or password is not right. Please check it and try again.'
    ERROR_INVALID_PROMO = 'Oops. This promo code is invalid. Please check it and try again'
    ERROR_PROMO_ALREADY_USED = 'Oops. You already used this promo code.'
    ERROR_RECOVERY_LINK_IS_INVALID = 'Oops. This recovery link is invalid. Please check it and try again.'
    ERROR_SHORT_PASSWORD = 'Oops. Your password should be 8 characters in length.'

    SUCCESS_CREDITS_PROMO_ACTIVATED = "Congratulation! Promo code {} activated. You've got {} credits on account."
    SUCCESS_DISCOUNT_PROMO_ACTIVATED = "Congratulation! Promo code {} activated. You've got {}% discount."
    SUCCESS_EMAIL_CONFIRMED = 'Congratulations! Your email successfully confirmed.'
    SUCCESS_PASSWORD_CHANGED = 'Congratulations! Your password successfully changed!'

    WARNING_SOMETHING_WENT_WRONG = 'Warning! Something went wrong. Please forgive us and try again.'

    PAGE_INDEX = {'button_submit': 'Submit',
                  'label_file': 'Choose file',
                  'tab_settings': 'Settings',
                  'tab_upload': 'Upload',
                  'title': 'Online Cinema',
                  }

    PAGE_RESET_PASSWORD = {'button_submit': 'Submit',
                           'label_password': 'Password',
                           'placeholder_password': 'Enter new password...',
                           'tab_restore': 'Password recovery',
                           'title': 'Online Cinema | Password recovery'
                           }

    PAGE_RESTORE = {'button_submit': 'Submit',
                    'label_email': 'Email',
                    'placeholder_email': 'Enter email...',
                    'tab_restore': 'Password recovery',
                    'title': 'Online Cinema | Password recovery'
                    }

    PAGE_SIGN_IN = {'button_login': 'Login',
                    'button_register': 'Register',
                    'label_email': 'Email',
                    'label_first_name': 'First Name',
                    'label_last_name': 'Last Name',
                    'label_password': 'Password',
                    'link_recovery_password': 'Forgot your password?',
                    'placeholder_email': 'Enter email...',
                    'placeholder_first_name': 'Enter your First Name...',
                    'placeholder_last_name': 'Enter your Last Name...',
                    'placeholder_password': 'Enter password...',
                    'tab_sign_in': 'Sign In',
                    'tab_sign_up': 'Sign Up',
                    'title': 'Online Cinema | Sign In',
                    }

    def __str__(self):
        return 'en-us'


__language_codes = {
    'ru-ru': RuRu(),
    'en-us': EnUs(),
}


def get_resources(request=None):
    try:
        if request.user.is_authenticated:
            return __language_codes[request.user.lang]
        else:
            return __language_codes[request.session['lang']]
    except KeyError:
        return __language_codes['en-us']


if __name__ == '__main__':
    res = get_resources()
    a = []
    for key, value in res.PAGE_SIGN_IN.items():
        a.append(key)
    a.sort()
    for i in a:
        print(i)
