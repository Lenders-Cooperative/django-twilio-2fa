# Django 2FA using Twilio Verify

## Prerequisites

* Python 3.6+
* [Twilio](https://twilio.com) account
* `django` 2.29+
* `twilio` 7.8.2+
* `phonenumbers` 8.12.47+

## Installation

Install using `pip install django-twilio-2fa`.

Add to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    ...
    "django_twilio_2fa",
    "django_widget_tweaks",  # only required if using included templates
    ...
)
```

Add the project `urls.py`:
```python
urlpatterns = [
    ...
    path(
        "2fa/",
        include("django_twilio_2fa.urls")
    ),
]
```

## Settings

All settings are prefixed with `TWILIO_2FA_`.

Any of the settings can be a callback. However, settings ending with `_CB` **must** be a callback. If a callback setting is defined but is not callable, a `ValueError` will be thrown.

### `ACCOUNT_SID`

Your Twilio account SID from the Twilio Console.

_Note: You cannot use test credentials with Verify._

### `AUTH_TOKEN`

Your Twilio auth token from the Twilio Console.

_Note: You cannot use test credentials with Verify._

### `SERVICE_ID`

Verify service ID from the Twilio Console.

### `ALLOWED_METHODS`

A list of allowed methods. The method must be enabled in the Verify service you setup in the Twilio Console.

Available methods: `sms`, `call`, and `whatsapp`. _Note: `email` is currently not supported._

If this setting is `None` or not set, all available methods will be presented to the end user.

### `ALLOW_REGISTER`

Indicates whether users should be allowed to register their phone number if one does not already exist. 

If this is `False` and the user has no phone number, they will not be able to use 2FA.

Defaults to `True`.

### `RETRY_TIME`

Amount of time (in seconds) after the last delivery attempt to allow the user to reattempt delivery of the verification.

Twilio does not have a limit on the amount of time between retries.

Defaults to 180 seconds or 3 minutes.

### `VERIFY_SUCCESS_URL`

The URL to redirect users to after a successful verification. This _should not_ return a `Response` instead (like `HttpResponseRedirect`) and should only return the URL as a string.

Defaults to `reverse_lazy("twilio_2fa:success")`

### `SERVICE_NAME`

Overrides the Verify service's friendly name set in the Twilio Console.

Arguments sent if callable:
* `user`: User instance
* `request`: `Request` instance
* `method`: Method string
* `phone_number`: Phone number string

Defaults to `None` (no override).

### `REGISTER_CB`

This callback is triggered when the user registers their phone number and should be used to update the user.

Arguments sent to this callback:
* `user`: User instance
* `phone_number`: Phone number string

No return is expected with this callback. 

### `PHONE_NUMBER_CB`

This callback is triggered on each verification request and should return the user's phone number.

Arguments sent to this callback:
* `user`: User instance

Expected return of this callback:
* String of the user's phone number

### `METHOD_DISPLAY_CB`

This callback is triggered on each request and allows customization of the method icon and label.

Arguments sent to this callback:
* `method`: Method string

Expected return of this callback is a `dict` with one or more of the following values (the default will be used if not included):
* `icon`: Font Awesome 5 icon classes (return `None` to not use an icon)
* `label`: Label string

## Signals

All signal names are prefixed `twilio_2fa_`.

### `verification_sent`

This signal is triggered anytime a verification is sent. 

Arguments sent with this signal:
* `twilio_sid`: The SID for this user's verification
* `user`: The user instance
* `phone_number`: Phone number
* `method`: Method name
* `timestamp`: `DateTime` instance

## Customization

The presentation code uses [Bootstrap 5](https://getbootstrap.com/docs/5.1/), [Font Awesome 5](https://fontawesome.com/v5/search), and [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks). None are an absolute requirement and can be removed using custom templates or, in the case of Font Awesome, defining the `METHOD_DISPLAY_CB` setting.

### `_base.html`

This is the primary template that all main templates extends.

It defines a single block for content: `content`. For `django_widget_tweaks`, the `content` block is wrapped by `WIDGET_ERROR_CLASS`. 

### `_messages.html`

This template shows messages from `django.contrib.messages` and is included in each of the main templates.

### `failed.html`

This template is shown when the user's verification failed either from a timeout of the verification, maximum tries are exceeded, an API failure with Twilio, or other general error.

It conditionally allows users to retry verification based on the `can_retry` session variable.

### `register.html`

This template shows the registration form to the user.

If `ALLOW_REGISTRATION` is `False`, the user is not shown this view and will be redirected to the failure page if no phone number is returned by `PHONE_NUMBER_CB`.

### `start.html`

This template allows the user to select the verification method.

If only one method exists, the user will not see this page.

### `success.html`

This template is shown on a successful verification if `VERIFY_SUCCESS_URL` is not set.

### `verify.html`

This template shows the token form.

## Development

Perform the following steps in the root directory:

1. Create a virtual environment and activate.
2. Install `django_twilio_2fa`: `pip install -e .`

Perform the following steps in the `test_app` directory:

3. Install requirements: `pip install -r requirements.txt`.
4. Copy `.env-sample` to `.env` and update with your settings.
5. Run migrations: `python manage.py migrate`.
6. Run the server: `python manage.py runserver`.

The test app should now be available at http://localtest.me:8000.
