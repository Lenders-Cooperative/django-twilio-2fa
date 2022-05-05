from django.urls import path, include
from .views import *


app_name = "twilio_2fa"


urlpatterns = [
    path(
        "",
        Twilio2FAIndexView.as_view(),
        name="index",
    ),
    path(
        "register",
        Twilio2FARegisterView.as_view(),
        name="register"
    ),
    path(
        "start",
        Twilio2FAStartView.as_view(),
        name="start"
    ),
    path(
        "verify",
        Twilio2FAVerifyView.as_view(),
        name="verify"
    ),
    path(
        "success",
        Twilio2FASuccessView.as_view(),
        name="success"
    ),
    path(
        "failed",
        Twilio2FAFailedView.as_view(),
        name="failed"
    )
]
