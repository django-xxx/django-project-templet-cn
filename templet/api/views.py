# -*- coding: utf-8 -*-

from utils.error.response_utils import response


def mail_error_test(request):
    # Raise ZeroDivisionError
    1 / 0
    return response()
