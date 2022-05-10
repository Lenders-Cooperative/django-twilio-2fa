from datetime import datetime, timedelta, timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_twilio_2fa.utils import *


class Require2faMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def has_2fa_expired(self, request):
        last_attempt = request.user.profile.last_2fa_attempt

        if not last_attempt:
            return True

        try:
            if datetime.now(tz=last_attempt.tzinfo) > (last_attempt + timedelta(minutes=30)):
                return True

        except ValueError:
            return True

        return False

    def is_2fa_required(self, request):
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            return True

        return False

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if "static" in request.path or (request.resolver_match and URL_PREFIX in request.resolver_match.view_name):
            return

        if self.is_2fa_required(request) and self.has_2fa_expired(request):
            return HttpResponseRedirect(
                reverse(f"{URL_PREFIX}start")
            )
