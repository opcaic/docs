.. _webapp-configuration:

#####################
Web app configuration
#####################

The web application uses several configuration variables which can be used to customize the
application behavior. Variables can be set in the ``env/.env`` file (or ``env/.env.development`` for
development builds). The variables must be set before the application is built.

*******
General
*******

API_URL
    URL of the API server. If the API is located on ``http://example.com/api/tournaments``, the
    ``API_URL`` would be ``http://example.com/``. If both the web app and the API server are
    accessible from the same domain, the ``API_URL`` can be set to ``/``. Default ``/``.

APP_NAME
    Name of the application. Is displayed in the title of the application and sometimes instead of a
    logo. Default ``OPCAIC``.

AUTH_REFRESH_PERIOD_SECONDS
    How often should the application ask backend for a new authorization refresh token. Default
    ``1800`` seconds.

AUTH_REMEMBER_ME_DAYS
    For how long should the authorization information be stored in the browser when users want to
    remember their logins. Default ``30`` days.

PRIVACY_POLICY_URL
    URL of the privacy policy that must be accepted when user registers.

CAPTCHA_KEY
    Google reCAPTCHA v2 API key.
