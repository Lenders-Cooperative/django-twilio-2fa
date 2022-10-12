# Available Settings

### `TWILIO_2FA_ACCOUNT_SID`

Twilio account SID



### `TWILIO_2FA_ALLOWED_METHODS`

List of methods setup in your Verify service



### `TWILIO_2FA_ALLOW_CHANGE`

Indicates if a user is allowed to change 2FA phone number


If callable, the following kwargs are sent:
 * `user`


### `TWILIO_2FA_ALLOW_REGISTRATION`

Indicates if a user is allowed to register a phone number for 2FA


If callable, the following kwargs are sent:
 * `user`


### `TWILIO_2FA_ALLOW_UNAUTHENTICATED_USERS`

Allow verification outside of an authenticated user session



### `TWILIO_2FA_ALLOW_USERLESS`

Allow verification without any user



### `TWILIO_2FA_ALLOW_USER_CB`
_This setting must be a callable._

Indicates if a user is allowed to use 2FA verification


If callable, the following kwargs are sent:
 * `user`


### `TWILIO_2FA_ALLOW_USER_ERROR_REDIRECT`

Redirect URL when a user is not allowed to verify


If callable, the following kwargs are sent:
 * `user`


### `TWILIO_2FA_AUTH_TOKEN`

Twilio account auth token



### `TWILIO_2FA_CANCEL_ON_MAX_RETRIES`

If a user reaches max attempts, cancel verification -- user will be unable to verify again until the current verification has expired or been canceled



### `TWILIO_2FA_DEFAULT_ERROR_CODE`

Default error code when an unknown error is thrown



### `TWILIO_2FA_DEFAULT_ERROR_DISPLAY`

Default error message displayed to user



### `TWILIO_2FA_ERROR_DISPLAY_CB`
_This setting must be a callable._

Override of error message displayed to user based on given code


If callable, the following kwargs are sent:
 * `code`


### `TWILIO_2FA_IS_VERIFIED_CB`
_This setting must be a callable._

Indicates if a user has been verified


If callable, the following kwargs are sent:
 * `request`


### `TWILIO_2FA_MAX_ATTEMPTS`

Maximum attempts allowed (configurable through Twilio)



### `TWILIO_2FA_MAX_SENDS`

Maximum number of sends (configurable through Twilio)



### `TWILIO_2FA_PHONE_NUMBER_ALLOWED_CARRIER_TYPES`





### `TWILIO_2FA_PHONE_NUMBER_ALLOWED_COUNTRIES`

List of ISO country codes where phone numbers are allowed



### `TWILIO_2FA_PHONE_NUMBER_BYPASS_CARRIER_ON_EMPTY`





### `TWILIO_2FA_PHONE_NUMBER_CARRIER_LOOKUP`

Perform a carrier lookup using Twilio Lookup service



### `TWILIO_2FA_PHONE_NUMBER_DEFAULT_REGION`

Default ISO country code for phone numbers



### `TWILIO_2FA_PHONE_NUMBER_DISALLOWED_COUNTRIES`

List of ISO country codes where phone numbers are not allowed (overrides allowed country codes)



### `TWILIO_2FA_SEND_COOLDOWN`

Seconds allowed between sending verifications



### `TWILIO_2FA_SERVICE_ID`

Twilio Verify service SID



### `TWILIO_2FA_SERVICE_NAME`

Friendly name to be used for Twilio Verify (defaults to friendly name of service)


If callable, the following kwargs are sent:
 * `request`


### `TWILIO_2FA_SUCCESS_REDIRECT_URL`

URL to redirect user to after a successful verification, if `next` is not set


If callable, the following kwargs are sent:
 * `user`


### `TWILIO_2FA_UNAUTHENTICATED_QUERY_PARAM`

URL query parameter used to specify the field on the user model



### `TWILIO_2FA_UNAUTHENTICATED_USER_FIELD`

User model field to compare value of query parameter



### `TWILIO_2FA_USER_EMAIL_CB`
_This setting must be a callable._

Return a user's e-mail address as an `Email` instance


If callable, the following kwargs are sent:
 * `user`


### `TWILIO_2FA_USER_METHODS_CB`
_This setting must be a callable._

List of methods a user is allowed to verify with (will default to allowed methods)


If callable, the following kwargs are sent:
 * `user`


### `TWILIO_2FA_USER_PHONE_NUMBER_CB`
_This setting must be a callable._

Return a user's phone number as a `PhoneNumber` instance


If callable, the following kwargs are sent:
 * `user`


### `TWILIO_2FA_VERIFICATION_EXPIRATION`

Verification expiration in minutes (contact Twilio support to change)



