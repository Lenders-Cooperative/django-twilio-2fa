from datetime import datetime
from django.dispatch import receiver
from django_twilio_2fa.dispatch import twilio_2fa_verification_success, twilio_2fa_verification_retries_exceeded


__all__ = [
    "handle_2fa_success", "handle_2fa_retries_exceeded"
]


@receiver(twilio_2fa_verification_success, sender=None)
def handle_2fa_success(signal, user, **kwargs):
    user.profile.last_2fa_attempt = datetime.now()
    user.profile.save()


@receiver(twilio_2fa_verification_retries_exceeded, sender=None)
def handle_2fa_retries_exceeded(signal, user, phone_number, method, twilio_sid, timeout, timeout_until, **kwargs):
    user.profile.timeout_for_2fa = timeout_until
    user.profile.save()
