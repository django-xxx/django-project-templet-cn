# -*- coding: utf-8 -*-

from django.http import JsonResponse
from StatusCode import StatusCodeField


def response_data(status_code=200, message=None, description=None, data={}, **kwargs):
    return dict({
        'status': status_code,
        'message': message,
        'description': description,
        'data': data,
    }, **kwargs)


def response(status_code=200, message=None, description=None, data={}, **kwargs):
    message, description = (message or status_code.message, description or status_code.description) if isinstance(status_code, StatusCodeField) else (message, description)
    return JsonResponse(response_data(status_code, message, description, data, **kwargs), safe=False)
