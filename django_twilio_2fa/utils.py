from django.conf import settings
from django.core.exceptions import ValidationError
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from twilio.rest import Client as TwilioClient
from .conf import *


__all__ = [
    "get_twilio_client", "verify_phone_number",
]


def get_twilio_client(**kwargs):
    if "account_sid" not in kwargs:
        kwargs["account_sid"] = get_setting("ACCOUNT_SID")
        kwargs["auth_token"] = get_setting("AUTH_TOKEN")

    args = [
        kwargs.pop("account_sid"),
        kwargs.pop("auth_token"),
    ]

    return TwilioClient(*args, **kwargs)


def verify_phone_number(phone_number, do_lookup=False):
    try:
        phone_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(phone_number):
            raise ValidationError({
                "phone_number": "Invalid phone number"
            })
    except NumberParseException as e:
        raise ValidationError({
            "phone_number": "Phone Number must be 10 digits"
        })

    if do_lookup:
        invalid_number = ValidationError({
            "phone_number": "Could not verify phone number. Make sure its a valid US-based mobile number."
        })

        try:
            response = get_twilio_client().lookups \
                .phone_numbers(
                phone_number.national_number
            ).fetch(
                type=["carrier"]
            )

            if not response.country_code == "US" or not response.carrier.get("type", "") == "mobile":
                raise invalid_number

        except Exception:
            raise invalid_number

    return True
