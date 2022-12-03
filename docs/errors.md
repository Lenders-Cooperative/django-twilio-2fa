# Errors


Error classes are located in `django_twilio_2fa.errors` and are `Exception` subclasses. 

When using the API endpoints, errors are returned as a JSON object:
```json
{
    "success": false,
    "error_code": "<error_code>",
    "display": "<user_display>",
    "data": "<obj>",
    "blocking": <true or false>
}
```


## `BadUserData`

* **Error code:** `bad_user_data`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `400`
* **Should block further attempts?** No


## `ChangeNotAllowed`

* **Error code:** `change_not_allowed`
* **Display for user:** `You cannot change your {field_display}`
* **Status Code:** `500`
* **Should block further attempts?** No


## `EmailNotSet`

* **Error code:** `email_not_set`
* **Display for user:** `An e-mail address is not set for your account.`
* **Status Code:** `500`
* **Should block further attempts?** No


## `GenericTwilioError`

* **Error code:** `twilio_error_{twilio_error}`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `500`
* **Should block further attempts?** No


## `InvalidCarrierType`

* **Error code:** `invalid_carrier_type`
* **Display for user:** `{carrier_type} phone numbers are not allowed`
* **Status Code:** `400`
* **Should block further attempts?** No


## `InvalidPhoneNumber`

* **Error code:** `invalid_phone_number`
* **Display for user:** `Invalid phone number`
* **Status Code:** `400`
* **Should block further attempts?** No


## `MalformedRequest`

* **Error code:** `malformed_request`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `400`
* **Should block further attempts?** No


## `MaxAttemptsReached`

* **Error code:** `max_attempts_reached`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `400`
* **Should block further attempts?** No


## `MaxSendsReached`

* **Error code:** `max_sends_reached`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `400`
* **Should block further attempts?** No


## `MethodNotAllowed`

* **Error code:** `method_not_allowed`
* **Display for user:** `The method {method} selected cannot be used at this time`
* **Status Code:** `400`
* **Should block further attempts?** No


## `MissingUserData`

* **Error code:** `missing_user_data`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `404`
* **Should block further attempts?** No


## `MobileNumberRequired`

* **Error code:** `mobile_number_required`
* **Display for user:** `To use {method_label}, you must have a mobile number`
* **Status Code:** `400`
* **Should block further attempts?** No


## `NoMethodAvailable`

* **Error code:** `no_method_available`
* **Display for user:** `No method available for verification`
* **Status Code:** `500`
* **Should block further attempts?** Yes


## `PhoneCountryNotAllowed`

* **Error code:** `phone_country_not_allowed`
* **Display for user:** `We do not allow phone numbers originating from {country_code}`
* **Status Code:** `400`
* **Should block further attempts?** No


## `PhoneNumberNotSet`

* **Error code:** `phone_not_set`
* **Display for user:** `A phone number is not set for your account.`
* **Status Code:** `500`
* **Should block further attempts?** No


## `RegistrationNotAllowed`

* **Error code:** `registration_not_allowed`
* **Display for user:** `You cannot set your 2FA {field_display}`
* **Status Code:** `500`
* **Should block further attempts?** No


## `SendCooldown`

* **Error code:** `resend_cooldown`
* **Display for user:** `Please wait before resending your verification`
* **Status Code:** `500`
* **Should block further attempts?** No


## `TwilioRateLimited`

* **Error code:** `twilio_rate_limited`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `500`
* **Should block further attempts?** No


## `UnauthenticatedUserFieldMissing`

* **Error code:** `unauthenticated_user_field_missing`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `500`
* **Should block further attempts?** No


## `UnauthenticatedUserParamMissing`

* **Error code:** `unauthenticated_user_param_missing`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `400`
* **Should block further attempts?** No


## `UserCannotVerify`

* **Error code:** `user_cannot_verify`
* **Display for user:** `You cannot verify at this time.`
* **Status Code:** `401`
* **Should block further attempts?** Yes


## `UserNotAllowed`

User is not allowed to verify

* **Error code:** `user_not_allowed`
* **Display for user:** `You are not allowed to verify at this time`
* **Status Code:** `403`
* **Should block further attempts?** No


## `UserNotFound`

* **Error code:** `user_not_found`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `404`
* **Should block further attempts?** No


## `UserRequired`

* **Error code:** `user_required`
* **Display for user:** `A user is required for 2FA`
* **Status Code:** `500`
* **Should block further attempts?** Yes


## `UserUnauthenticated`

* **Error code:** `user_unauthenticated`
* **Display for user:** `You must be logged in`
* **Status Code:** `401`
* **Should block further attempts?** No


## `VerificationNotFound`

* **Error code:** `verification_not_found`
* **Display for user:** `Unable to verify at this time`
* **Status Code:** `404`
* **Should block further attempts?** No


