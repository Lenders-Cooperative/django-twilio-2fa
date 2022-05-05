from django import forms


__all__ = [
    "Twilio2FARegistrationForm", "Twilio2FAVerifyForm",
]


class Twilio2FARegistrationForm(forms.Form):
    phone_number = forms.CharField()

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"]
        transtab = str.maketrans("", "", "()-. _")
        return phone.translate(transtab)


class Twilio2FAVerifyForm(forms.Form):
    token = forms.CharField(
        required=True
    )
