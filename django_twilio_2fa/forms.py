from django import forms
from django.core.exceptions import ValidationError
import pycountry

from .app_settings import conf


__all__ = [
    "Twilio2FARegistrationForm", "Twilio2FAVerifyForm", "CountryCodeField",
]


class CountryCodeField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs["choices"] = [
            ("", "--"),
        ]

        country_codes = list(set(conf.allowed_countries()) - set(conf.disallowed_countries()))
        country_codes.sort()

        for c in country_codes:
            country = pycountry.countries.get(alpha_2=c)

            if country:
                kwargs["choices"].append((c, country.name))
            else:
                raise ValueError(f"{c} is not a valid alpha_2 country code")

        super().__init__(*args, **kwargs)


class Twilio2FARegistrationForm(forms.Form):
    country_code = CountryCodeField()
    phone_number = forms.CharField()


class Twilio2FAVerifyForm(forms.Form):
    token = forms.CharField(
        required=True
    )

    def clean_token(self):
        token = self.cleaned_data["token"]

        if len(str(token)) != conf.token_length() or not str(token).isnumeric():
            raise ValidationError(f"Please provide a valid {conf.token_length()} digit token")

        return token
