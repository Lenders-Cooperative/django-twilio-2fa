# Available Settings

All settings must be prefixed with `TWILIO_2FA_`.

### `ACCOUNT_SID`

Your Twilio account SID from the Twilio Console.

_Note: You cannot use test credentials with Verify._

Defaults to: `None`


### `ALLOWED_METHODS`

List of methods setup in your Verify service. The method must be enabled in the Verify service you setup in the Twilio Console.

Available methods: `sms`, `call`, `email` and `whatsapp`. 
_Note: `email` requires a Sendgrid integration.Details can be found [here](https://www.twilio.com/docs/verify/email#create-an-email-template)._

If this setting is `None` or not set, all available methods will be presented to the end user.

Defaults to: `[]`


### `ALLOW_CHANGE`

Indicates if a user is allowed to change 2FA phone number

Defaults to: `True`

If callable, the following kwargs are sent:
 * `user`


### `ALLOW_REGISTRATION`

Indicates if a user is allowed to register a phone number for 2FA

Defaults to: `True`

If callable, the following kwargs are sent:
 * `user`


### `ALLOW_UNAUTHENTICATED_USERS`

Allow verification outside of an authenticated user session

Defaults to: `False`


### `ALLOW_USERLESS`

Allow verification without any user

Defaults to: `False`


### `ALLOW_USER_CB`
_This setting must be a callable._

Indicates if a user is allowed to use 2FA verification.

This setting is useful if you have users that are verified outside of the normal flow (such as SSO).

Defaults to: `True`

If callable, the following kwargs are sent:
 * `user`


### `API_CLASSES`

Dictionary of classes list to apply to API views.

Accepted keys:
* `permission`
* `authentication`
* `throttle`

(Only applicable to API-based 2FA.)

Defaults to: `{}`


### `AUTH_TOKEN`

Your Twilio account token from the Twilio Console.

_Note: You cannot use test credentials with Verify._

Defaults to: `None`


### `CANCEL_ON_MAX_RETRIES`

If a user reaches max attempts, cancel verification -- user will be unable to verify again until the current verification has expired or been canceled

Defaults to: `False`


### `DEFAULT_ERROR_CODE`

Default error code when an unknown error is thrown

Defaults to: `2fa_error`


### `DEFAULT_ERROR_DISPLAY`

Default error message displayed to user

Defaults to: `Unable to verify at this time`


### `DISALLOWED_REDIRECT_URL`

Redirect URL when a user is not allowed to verify.

(Applicable only to view-based 2FA.)

Defaults to: `/`

If callable, the following kwargs are sent:
 * `user`


### `ERROR_DISPLAY_CB`
_This setting must be a callable._

Allows overriding of error messages displayed to user.

The [error code](errors.md) is sent and the string or gettext_lazy

Defaults to: `{}`

If callable, the following kwargs are sent:
 * `code`


### `HAS_CLNPC_PERMISSION`

To perform a lookup on a Canadian number, you must have permission from the CLNPC and you account must be updated by Twilio support.

See [this Twilio support article](https://support.twilio.com/hc/en-us/articles/360004563433).

Defaults to: `False`


### `MAX_ATTEMPTS`

Maximum attempts allowed (configurable through Twilio)

Defaults to: `5`


### `MAX_SENDS`

Maximum number of sends (configurable through Twilio)

Defaults to: `5`


### `METHOD_DETAILS`

Allows overriding a verification method's details like icon and display text.

This setting should return a dictionary with one or more methods and the overrides in a nested dictionary.

Each method can define one or both of the following:
* `label` - Method name displayed to user
* `icon` - Icon class (from places like [FontAwesome](https://fontawesome.com/))

Defaults to: `{}`


### `PHONE_NUMBER_ALLOWED_CARRIER_TYPES`

A list of allowed carrier types.

Available types: `voip`, `landline`, and `mobile`.

_Note: not all countries provide this information._

Defaults to: `['mobile']`


### `PHONE_NUMBER_ALLOWED_COUNTRIES`

List of country codes from which phone numbers are allowed to originate.

Defaults to: `['US']`


### `PHONE_NUMBER_BYPASS_CARRIER_ON_EMPTY`

Allow bypassing if the carrier information is empty on lookup

Defaults to: `True`


### `PHONE_NUMBER_CARRIER_LOOKUP`

Perform a carrier lookup using Twilio Lookup service

Defaults to: `True`


### `PHONE_NUMBER_DEFAULT_REGION`

Default ISO country code for phone numbers.

The default region for [`phonenumbers`](https://github.com/daviddrysdale/python-phonenumbers) library. Typically, this is the country code, but the entire list can be found [here](https://github.com/daviddrysdale/python-phonenumbers/tree/dev/python/phonenumbers/data).

Setting this allows users to not need to enter a country code with their phone number. 

You can set this to `None` to not have a default region.

Defaults to: `US`


### `PHONE_NUMBER_DISALLOWED_COUNTRIES`

List of country codes from which phone numbers *are not* allowed to originate. 

These countries are *removed* from the allowed countries list.

Defaults to: `[]`


### `SEND_COOLDOWN`

Seconds after the last delivery attempt to allow the user to reattempt delivery of the verification.

Twilio does not have a limit on the amount of time between retries.

Defaults to: `30`


### `SEND_IMMEDIATELY_ON_SINGLE`

If only one verification method is available, skip method selection and send immediately.

(Only applicable to view-based 2FA.)

Defaults to: `True`


### `SERVICE_ID`

Your Twilio Verify service SID from the Twilio Console.

Defaults to: `None`


### `SERVICE_NAME`

Overrides the Verify service's friendly name set in the Twilio Console.

Defaults to: `None`

If callable, the following kwargs are sent:
 * `request`


### `SUCCESS_REDIRECT_URL`

The URL to redirect users to after a successful verification. This _should not_ return a `Response` (like `HttpResponseRedirect`) and should only return the URL as a string.

(Only applicable to view-based 2FA.)

Defaults to: `None`

If callable, the following kwargs are sent:
 * `user`


### `UNAUTHENTICATED_QUERY_PARAM`

URL query parameter used to specify the field on the user model

Defaults to: `user_id`


### `UNAUTHENTICATED_USER_FIELD`

User model field to compare value of query parameter

Defaults to: `pk`


### `USER_EMAIL_CB`
_This setting must be a callable._

Return a user's e-mail address as an `django_twilio_2fa.options.Email` instance

Defaults to: `None`

If callable, the following kwargs are sent:
 * `user`


### `USER_METHODS_CB`
_This setting must be a callable._

List of methods a user is allowed to verify with.

By default, the methods allowed for a user is determined based on data available.
For example, a user with a phone number but no carrier type wouldn't be able to use the `sms` method.

Defaults to: `None`

If callable, the following kwargs are sent:
 * `user`


### `USER_MUST_HAVE_PHONE`

If a user does not have a phone number, they must register one to verify.

Defaults to: `False`


### `USER_PHONE_NUMBER_CB`
_This setting must be a callable._

Return a user's phone number as a `django_twilio_2fa.options.PhoneNumber` instance

Defaults to: `None`

If callable, the following kwargs are sent:
 * `user`


### `VERIFICATION_EXPIRATION`

Verification expiration in minutes (contact Twilio support to change)

Defaults to: `10`


