from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_twilio_2fa.utils import *


class Require2faMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def has_2fa_expired(self, request):
        timestamp = request.session.get("twilio_2fa_timestamp")

        if not timestamp:
            return True

        try:
            timestamp = datetime.strptime(timestamp, DATEFMT)

            if datetime.now() > (timestamp + timedelta(minutes=30)):
                return True

        except ValueError:
            return True

        return False

    def is_2fa_required(self, request):
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            return True

        return False

    def __call__(self, request):
        response = self.get_response(request)

        if "static" in request.path or (request.resolver_match and request.resolver_match.app_name == URL_PREFIX):
            return response

        if self.is_2fa_required(request) and self.has_2fa_expired(request):
            return HttpResponseRedirect(
                reverse(f"{URL_PREFIX}:start")
            )

        return response
