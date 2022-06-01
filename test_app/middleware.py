from datetime import datetime, timedelta, timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_twilio_2fa.utils import *
from django.contrib import messages


class Require2faMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def has_2fa_expired(self, request):
        expiration = request.session.get("twilio_2fa_expiration", "20000101000000")

        try:
            expiration = datetime.strptime(expiration, "%Y%m%d%H%M%S")
        except ValueError:
            expiration = None

        return not expiration or datetime.now() > expiration

    def is_2fa_required(self, request):
        if not request.user.is_authenticated:
            return False

        if not request.session.get("is_post_login", False):
            return False

        if "is_post_login" in request.session:
            del request.session["is_post_login"]

        return True

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if "static" in request.path or (request.resolver_match and URL_PREFIX in request.resolver_match.view_name):
            return

        if self.is_2fa_required(request) and self.has_2fa_expired(request):
            next_url = reverse(
                request.resolver_match.view_name,
                kwargs=view_kwargs,
                args=view_args
            )
            return HttpResponseRedirect(
                f"{reverse(f'{URL_PREFIX}:start')}?next={next_url}"
            )
