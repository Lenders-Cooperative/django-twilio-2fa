from datetime import datetime, timedelta
from django.dispatch import receiver
from django_twilio_2fa.dispatch import twilio_2fa_verification_success, twilio_2fa_verification_retries_exceeded
from django.contrib.auth.signals import user_logged_in


__all__ = [
    "handle_2fa_success", "handle_2fa_retries_exceeded", "set_post_login_session",
]


@receiver(user_logged_in, sender=None)
def set_post_login_session(sender, request, user, **kwargs):
    request.session["is_post_login"] = True


@receiver(twilio_2fa_verification_success, sender=None)
def handle_2fa_success(signal, request, user, **kwargs):
    user.profile.last_2fa_attempt = datetime.now()
    user.profile.save()

    request.session["twilio_2fa_expiration"] = (datetime.now() + timedelta(seconds=60)).strftime("%Y%m%d%H%M%S")


@receiver(twilio_2fa_verification_retries_exceeded, sender=None)
def handle_2fa_retries_exceeded(signal, request, user, timeout, timeout_until, **kwargs):
    user.profile.timeout_for_2fa = timeout_until
    user.profile.save()
