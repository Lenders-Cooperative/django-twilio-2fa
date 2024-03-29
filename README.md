# Django 2FA using Twilio Verify

## Prerequisites

* Python 3.6+
* [Twilio](https://twilio.com) account
* `django` 2.29+
* `twilio` 7.8.2+
* `phonenumbers` 8.12.26+

## Installation

Install using `pip install django-twilio-2fa`.

If install fails, try `pip install --upgrade pip`

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
    # View-based 2FA
    path(
        "2fa/",  # Can be changed to any path
        include("django_twilio_2fa.urls")
    ),
    # API-based 2FA
    path(
        "2fa-api/",  # Can be changed to any path
        include("django_twilio_2fa.api.urls")
    ),
    ...
]
```

## Other Pages

* [View-based 2FA Flow](docs/view_flow.md)
* [Settings](docs/settings.md)
* [Errors](docs/errors.md)

## Signals

Signal names are prefixed `twilio_2fa_`.

All signals are sent with at least the following arguments:
* `request`: Current `Request` instance or `None`
* `user`: `User` instance or `None`

### `twilio_error`

When the Twilio client throws an error, this signal is emitted -- whether the error was handled. 

This is a special signal that only provides the exception instance as `exc` and no other arguments.

### `set_user_data`

When a user registers or changes their 2FA data, this signal is emitted the updated information and should be used to update the user's instance.

Additional arguments sent with this signal:
 * `field`: field name (`phone_number` is the only option)
 * `value`: updated value

### `verification_sent`

This signal is triggered anytime a verification is sent. 

Additional arguments sent with this signal:
* `method`: Verification method
* `verification_sid`: Twilio SID for verification
* `start_timestamp`: `DateTime` of the original send
* `last_timestamp`: `DateTime` of the last send attempt

### `verification_success`

This signal is triggered when a user completes verification successfully.

The `verification_status_changed` signal is also triggered during a successful verification.

Additional arguments sent with this signal:
* `verification_sid`: Twilio verification SID

### `verification_status_changed`

This signal is triggered when the Twilio verification status is changed. 

Options for `status`: `approved` and `canceled`.

Additional arguments sent with this signal:
* `status`: Status verification was changed to
* `verification_sid`: Twilio verification SID

### `verification_failed`

This signal is triggered when the Twilio verification attempt has failed.

Additional arguments sent with this signal:
* `verification_sid`: Twilio verification SID


## Customization

The presentation code uses [Bootstrap 5](https://getbootstrap.com/docs/5.1/), [Font Awesome 5](https://fontawesome.com/v5/search), and [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks). None are an absolute requirement and can be removed using custom templates or, in the case of Font Awesome, defining the `METHOD_DISPLAY_CB` setting.

All templates are in the `twilio_2fa` directory. To override these templates, you can put your version in your own `twilio_2fa` directory anywhere your templates are stored.

<img src="docs/assets/customization-diagram.png" width="50%">

### `_base.html`

This is the primary template that all main templates extends.

It defines a single block for content: `content` (outlined in yellow above). For `django_widget_tweaks`, the `content` block is wrapped by `WIDGET_ERROR_CLASS`.

The header can also be changed using the `header` block (outlined in red). Header icon classes changed using the `header_icon_class` block (outlined in blue) and text changed using the `header_text` block (outlined in green). 

### `_messages.html`

This template shows messages from `django.contrib.messages` and is included in each of the main templates.

### `_form_errors.html`

This template displays a form field's errors. `field` should be passed in the context.

### `failed.html`

This template is shown when the user's verification failed either from a timeout of the verification, maximum tries are exceeded, an API failure with Twilio, or other general error.

It conditionally allows users to retry verification based on the `can_retry` session variable.

### `registration_form.html`

This template shows the registration form to the user and serves as the base template for `register.html` and `change.html`. 

### `register.html`

This template shows the registration form to the user.

If `ALLOW_REGISTRATION` is `False`, the user is not shown this view and will be redirected to the failure page if no phone number is returned by `PHONE_NUMBER_CB`.

It is based on `registration_form.html`.

### `change.html`

This template shows the change form to the user.

It is based on `registration_form.html`.

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
3. Update path to this package in the requirements.txt
4. Install requirements: `pip install -r requirements.txt`.
5. Copy `.env-sample` to `.env` and update with your twilio settings.
6. Run migrations: `python manage.py migrate`.
7. Run the server: `python manage.py runserver`.

The test app should now be available at http://localtest.me:8000.

To run tests, run `python manage.py test` from the `test_app` directory.

### To-Do

* ~~Internationalization~~
* [~~E-mail verification~~](https://www.twilio.com/docs/verify/email)
* WhatsApp integration
* [TOTP integration](https://www.twilio.com/docs/verify/quickstarts/totp)
* [Push for web integration](https://www.twilio.com/docs/verify/quickstarts/push-web)
* ~~Abstraction for 2FA outside of web flow~~

### Changelog

* 0.32 - bug fixes for lost users
* 0.31 - minor fix of `error_displays` setting
* 0.30 - added more messages for user displays; updated view-based templates to use messages; added `display` key to API-based responses
* 0.29 - downgraded requirements for inclusivity
* 0.28 - added better customization of user messaging
* 0.27 - allow sending verifications to different values; set default status code for errors to 400
* 0.26 - added handling of Twilio Error 60200
* 0.25 - bug fix for handling unauthenticated users
* 0.24 - refactored to abstract process; added API endpoints; allow for userless 2FA
* 0.23 - Twilio rate limiting error handling
* 0.22 - Added internationalization and e-mail verification (thanks to [jgoodsell-summitgrp](https://github.com/jgoodsell-summitgrp))
