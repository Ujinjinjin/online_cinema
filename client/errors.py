#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ShortPasswordError(Exception):
    pass


class InvalidEmailError(Exception):
    pass


def check_data(email=None, password=None):
    if email is not None and len(email) < 5:
        raise InvalidEmailError
    if password is not None and len(password) < 8:
        raise ShortPasswordError


if __name__ == '__main__':
    print()
    raise ShortPasswordError
