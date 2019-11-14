.. _server-configuration:

####################
Server configuration
####################

The server component uses several configuration variables which can be used to customize the
platform behavior. Variables can be set by command line parameters, ``appsettings.json``
configuration file or environment variables. The environment variables take precedence over the
configuration file and command line parameters take precedence over environment variables.

Names of the configuration variables are case insensitive. The name of the variable resembles a path
in a tree of configuration variables, with ``:`` character as segment separator. Since environment
variables may not contain ``:`` character, the corresponding environment variable can be obtained by
replacing them by **double** underscores (``__``), e.g. ``Emails:Port`` becomes ``Emails__Port``.


*******
General
*******

FrontendUrl
  Address where the web application is accessible. Used for generating links for emails.


******
Broker
******

Broker:Identity
  String identifier of the server used when communicating with workers. The identifier must be
  different from the one used by all w

Broker:ListeningAddress
  Address used for listening for workers. Must be in form ``tcp://[host]:[port]``. For example, to
  allow connections from the ``168.192.*.*`` subnet on port ``6000``, use ``tcp://168.192.0.0:6000``

Broker:TaskRetentionSeconds
  How many seconds to keep tasks for a certain game in a working queue when last worker who was
  capable of running given game disconnected. There is generally no need to change this setting.

Broker:HeartbeatConfig:HeartBeatInterval
  How many milliseconds between individual heartbeats between worker and broker.

Broker:HeartbeatConfig:Liveness
  How many heartbeats is a worker allowed to miss before being considered dead by the broker.

Broker:HeartbeatConfig:ReconnectIntervalInit
  How many milliseconds workers should wait before trying to reconnect to the broker for the first
  time after disconnecting.

Broker:HeartbeatConfig:ReconnectIntervalMax
  Upper bound for the exponential back off time for workers between reconnect attempts after
  disconnecting.

  
********
Security
********

Contains important configuration regarding platform security.

JWT Configuration
=================

Configuration of JWT bearer security mechanism used for user authentication.

Security:JWT:Key
  Symetric key used for creating the JWT Bearer tokens for authentication.

Security:JWT:AccessTokenExpirationMinutes
  How many minutes should issued JWT access token be valid.

Security:JWT:RefreshTokenExpirationDays
  How many days should issued JWT refresh token be valid. Refresh tokens are used for requesting new
  access tokens and are invalidated on password change. After expiring, new tokens can be obtained
  by authenticating via email and p

Security:JWT:WorkerTokenExpirationMinutes
  How many minutes should access tokens issued to workers be valid. These tokens allow workers to
  download/upload files necessary for the task execution.

.. _password-strength-config:

Password Strength Configuration
===============================

Following options configure minimal requirements for account passwords.

Security:Password:RequireDigit
  If true, password must contain a digit, default ``false``.

Security:Password:RequireLowercase
  If true, password must contain a lowercase ASCII character, default ``false``.

Security:Password:RequireUppercase
  If true, password must contain an uppercase ASCII character, default ``false``.

Security:Password:RequireNonAlphanumeric
  If true, password must contain a non-alphanumeric character, default ``false``.

Security:Password:RequiredUniqueChars
  Minimum number of unique characters which password must contain. Must be greater than zero,
  default ``1``.

Security:Password:RequiredLength
  Minimum number of total characters which password must contain. Must be at least 8, default ``8``.

*******
Storage
*******

Storage:Directory
  Path to directory used as general file storage. Submissions, additional files and result files
  will be stored there.

******
Emails
******

Emails:SmtpServerurl
  Url (without port) of the server used for sending emails.

Emails:Port
  Port on smtp server to connect to.

Emails:Username
  Username used to authenticate to the smtp server.

Emails:Password
  Password used to authenticate to the smtp server.

Emails:UseSsl
  Whether SSL connection should be enforced when communicating with the smtp server.

Emails:SenderAddress
  Email address to use as the sender address.


******
Limits
******

Global limits for uploaded files sizes.

Limits:MaxTournamentFileSize
  Maximum total size of additional files for a tournament.

Limits:MaxSubmissionFileSize
  Maximum total size of submission files.

Limits:MaxResultFileSize
  Maximum total size of task result files received from workers.

******************
 Request limiting
******************

This section contains configuration of the _`AspNetCoreRateLimit
<https://github.com/stefanprodan/AspNetCoreRateLimit>` library used to protect the server against
DoS attacks. It allows specifying rules for individual endpoints. More detailed information about
the library can be found at the library's github repository.

IpRateLimiting:EnableEndpointRateLimiting
  If set to false, then only the rules with ``*`` endpoint are applied.

IpRateLimiting:StackBlockedRequests
  If true, blocked requests will contribute to limits in other other rules.
  
IpRateLimiting:RealIpHeader
  Name of the HTTP header used to extract the IP address of the client when the application is
  hosted behind a reverse proxy.

.. todo: What header does nginx use?

IpRateLimiting:HttpStatusCode
  Status code returned by requests over the limit. Recommended value is 429 Too Many Requests

IpRateLimiting:IpWhitelist
  An array of Ip addresses (as strings) which should not be affected by rate limiting. You may
  specify a mask by using values such as ``192.168.0.0/24``.
  
IpRateLimiting:EndpointWhitelist
  List of endpoints which should not be affected by rate limiting. These can be used to exclude
  specific endpoints from general rules. format is ``{Method}:{Endpoint}``. For example to
  explicitly disable request limiting for GET requests to ``/api/users`` endpoint, use
  ``get:/api/users`` value.

IpRateLimiting:GeneralRules
  Array of individual request limiting rules. To set individual items from command line or
  environment variables, use ``IpRateLimiting:GeneralRules:``\ *index* or
  ``IPRATELIMITING__GENERALRULES__``\ *index* prefix, respectively, for properties of array items.
  
IpRateLimiting:GeneralRules:*i*:Endpoint
  The endpoint for which the rule is defined, if ``IpRateLimiting:EnableEndpointRateLimiting`` is
  true, then use syntax ``{Method}:{Endpoint}`` to specify the endpoint. Otherwise use ``*``.

IpRateLimiting:GeneralRules:*i*:Period
  Duration of the time window which in which requests should be limited. The value should be a
  natural number. You can use sufixes s, m, h, d to specify that the duration is in seconds,
  minutes, hours or days.

IpRateLimiting:GeneralRules:*i*:Limit
  How many requests are permited during the specified time windows.

IpRateLimiting:IpRules
  Array of specialized rules for specific IP addresses.

IpRateLimiting:IpRules:*i*:Ip
  Ip address for which additional rules are specified.

IpRateLimiting:IpRules:*i*:Rules
  Rules for the specified IP address. The format is same as in ``IpRateLimiting:GeneralRules``
  array.

*******
Serilog
*******

Used to configure the `Serilog <http://www.serilog.net>`_ Logging library. See `official
documentation <https://github.com/serilog/serilog-settings-configuration>`_ for further details.
