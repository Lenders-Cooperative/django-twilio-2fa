from datetime import datetime
from django.dispatch import receiver
from django_twilio_2fa.dispatch import twilio_2fa_verification_success


__all__ = [
    "handle_2fa_success",
]


@receiver(twilio_2fa_verification_success, sender=None)
def handle_2fa_success(signal, sender, user, **kwargs):
    user.profile.last_2fa_attempt = datetime.now()
    user.profile.save()
