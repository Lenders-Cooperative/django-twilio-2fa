from django import forms
from .utils import country_code_choices, verify_phone_number


__all__ = [
    "Twilio2FARegistrationForm", "Twilio2FAVerifyForm",
]


class Twilio2FARegistrationForm(forms.Form):
    country_code = forms.ChoiceField(choices=country_code_choices())
    phone_number = forms.CharField()

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"]
        country = self.cleaned_data["country_code"]
        transtab = str.maketrans("", "", "()-. _")
        phone.translate(transtab)

        verify_phone_number(phone, country, do_lookup=True)

        return phone


class Twilio2FAVerifyForm(forms.Form):
    token = forms.CharField(
        required=True
    )
