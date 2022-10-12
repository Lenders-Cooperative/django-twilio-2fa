from django.conf import settings
from django.utils.translation import gettext_lazy as _


class SettingError(Exception):
    def __init__(self, key):
        self.key = key


class MustBeCallable(SettingError):
    def __str__(self):
        return f"{self.key}: Must be callable"


class EagerCallable(SettingError):
    def __str__(self):
        return f"{self.key}: Cannot make a callable eager loading"


class MissingRequiredCallbackArgument(SettingError):
    def __str__(self):
        return f"Missing required callback argument: {self.key}"


class MissingRequiredSetting(SettingError):
    def __str__(self):
        return f"Missing required setting: {self.key}"


DJ_SETTING_PREFIX = "TWILIO_2FA"


class Constant(object):
    def __init__(self, value):
        self.value = value

    def __call__(self):
        return self.value


class Setting(object):
    def __init__(
            self,
            key,
            required=False,
            default=None,
            must_be_callable=False,
            cb_kwargs_required=None,
            description=None
    ):
        self.key = key.upper()
        self.required = required
        self.default = default
        self.cb_kwargs_required = cb_kwargs_required
        self.has_attr = False
        self.must_be_callable = must_be_callable
        self.description = description or ""

        if not self.key.startswith(DJ_SETTING_PREFIX):
            self.key = f"{DJ_SETTING_PREFIX}_{self.key}"

        if must_be_callable and not self.key.endswith("_CB"):
            self.key += "_CB"

        if required and not hasattr(settings, self.key):
            raise AttributeError(f"Cannot find setting {self.key}")

        if not hasattr(settings, self.key):
            return

        if must_be_callable and not callable(getattr(settings, self.key)):
            raise MustBeCallable(self.key)

    def __call__(self, default=None, **cb_kwargs):
        if not default and callable(self.default):
            default = self.default()
        elif not default:
            default = self.default

        if not hasattr(settings, self.key):
            return default

        getter = getattr(settings, self.key)

        if callable(getter):
            for arg in self.cb_kwargs_required:
                if arg in cb_kwargs:
                    continue
                raise MissingRequiredCallbackArgument(arg)

            value = getter(**cb_kwargs)
        else:
            value = getter

        if value is None:
            return default

        return value


class Conf(object):
    available_methods = Constant({
        "sms": {
            "value": "sms",
            "label": _("Text Message"),
            "icon": "fas fa-sms",
            "data_required": "phone_number",
            "carrier_required": "mobile"
        },
        "call": {
            "value": "call",
            "label": _("Phone Call"),
            "icon": "fas fa-phone",
            "data_required": "phone_number"
        },
        "email": {
            "value": "email",
            "label": _("E-mail"),
            "icon": "fas fa-envelope",
            "data_required": "email"
        },
        "whatsapp": {
            "value": "whatsapp",
            "label": _("WhatsApp"),
            "icon": "fab fa-whatsapp",
            "data_required": "phone_number"
        }
    })
    session_data_key = Constant(
        "twilio_2fa_data"
    )
    allowed_methods = Setting(
        "allowed_methods",
        default=list,
        description="List of methods setup in your Verify service"
    )
    disallowed_redirect = Setting(
        "allow_user_error_redirect",
        default="/",
        cb_kwargs_required=["user"],
        description="Redirect URL when a user is not allowed to verify"
    )
    is_user_verified = Setting(
        "is_verified",
        must_be_callable=True,
        default=False,
        cb_kwargs_required=["request"],
        description="Indicates if a user has been verified"
    )
    default_error_code = Setting(
        "default_error_code",
        default="2fa_error",
        description="Default error code when an unknown error is thrown"
    )
    default_error_display = Setting(
        "default_error_display",
        default=_("Unable to verify at this time"),
        description="Default error message displayed to user"
    )
    error_displays = Setting(
        "error_display",
        default=dict,
        must_be_callable=True,
        cb_kwargs_required=["code"],
        description="Override of error message displayed to user based on given code"
    )
    success_redirect_url = Setting(
        "success_redirect_url",
        cb_kwargs_required=["user"],
        description="URL to redirect user to after a successful verification, if `next` is not set"
    )
    allow_userless = Setting(
        "allow_userless",
        default=False,
        description="Allow verification without any user"
    )
    #
    # Unauthenticated Requests
    allow_unauthenticated_users = Setting(
        "allow_unauthenticated_users",
        default=False,
        description="Allow verification outside of an authenticated user session"
    )
    unauthenticated_query_param = Setting(
        "unauthenticated_query_param",
        default="user_id",
        description="URL query parameter used to specify the field on the user model"
    )
    unauthenticated_user_field = Setting(
        "unauthenticated_user_field",
        default="pk",
        description="User model field to compare value of query parameter"
    )
    #
    # Twilio
    twilio_account_sid = Setting(
        "account_sid",
        required=True,
        description="Twilio account SID"
    )
    twilio_auth_token = Setting(
        "auth_token",
        required=True,
        description="Twilio account auth token"
    )
    twilio_service_id = Setting(
        "service_id",
        required=True,
        description="Twilio Verify service SID"
    )
    twilio_service_name = Setting(
        "service_name",
        cb_kwargs_required=["request"],
        description="Friendly name to be used for Twilio Verify (defaults to friendly name of service)"
    )
    #
    # Twilio 2FA
    verification_expiration = Setting(
        "verification_expiration",
        default=10,  # minutes
        description="Verification expiration in minutes (contact Twilio support to change)"
    )
    send_cooldown = Setting(
        "send_cooldown",
        default=30,  # seconds
        description="Seconds allowed between sending verifications"
    )
    max_attempts = Setting(
        "max_attempts",
        default=5,
        description="Maximum attempts allowed (configurable through Twilio)"
    )
    max_sends = Setting(
        "max_sends",
        default=5,
        description="Maximum number of sends (configurable through Twilio)"
    )
    cancel_on_max_retries = Setting(
        "cancel_on_max_retries",
        default=False,
        description="If a user reaches max attempts, cancel verification -- user will be unable to verify again until "
                    "the current verification has expired or been canceled"
    )
    #
    # Phone numbers
    do_carrier_lookup = Setting(
        "phone_number_carrier_lookup",
        default=True,
        description="Perform a carrier lookup using Twilio Lookup service"
    )
    allowed_countries = Setting(
        "phone_number_allowed_countries",
        default=["US"],
        description="List of ISO country codes where phone numbers are allowed"
    )
    disallowed_countries = Setting(
        "phone_number_disallowed_countries",
        default=list,
        description="List of ISO country codes where phone numbers are not allowed (overrides allowed country codes)"
    )
    default_country_code = Setting(
        "phone_number_default_region",
        default="US",
        description="Default ISO country code for phone numbers"
    )
    allowed_carrier_types = Setting(
        "phone_number_allowed_carrier_types",
        default=["mobile"]
    )
    bypass_carrier_on_empty = Setting(
        "phone_number_bypass_carrier_on_empty",
        default=True
    )
    #
    # User
    allow_user_to_verify = Setting(
        "allow_user",
        must_be_callable=True,
        default=True,
        cb_kwargs_required=["user"],
        description="Indicates if a user is allowed to use 2FA verification"
    )
    allow_registration = Setting(
        "allow_registration",
        default=True,
        cb_kwargs_required=["user"],
        description="Indicates if a user is allowed to register a phone number for 2FA"
    )
    allow_change = Setting(
        "allow_change",
        default=True,
        cb_kwargs_required=["user"],
        description="Indicates if a user is allowed to change 2FA phone number"
    )
    user_methods = Setting(
        "user_methods",
        required=True,
        must_be_callable=True,
        cb_kwargs_required=["user"],
        description="List of methods a user is allowed to verify with (will default to allowed methods)"
    )
    user_phone_number = Setting(
        "user_phone_number",
        required=True,
        must_be_callable=True,
        cb_kwargs_required=["user"],
        description="Return a user's phone number as a `PhoneNumber` instance"
    )
    user_email = Setting(
        "user_email",
        required=True,
        must_be_callable=True,
        cb_kwargs_required=["user"],
        description="Return a user's e-mail address as an `Email` instance"
    )
    #
    # View-based settings
    next_session_key = Constant(
        "twilio_2fa_next"
    )


conf = Conf()
