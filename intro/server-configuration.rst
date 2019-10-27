####################
Server configuration
####################

The server component uses several configuration variables which can be used to customize the platform behavior. Variables can be set by command line parameters, ``appsettings.json`` configuration file or environment variables. The environment variables take precedence over the configuration file and command line parameters take precedence over environment variables.

Names of the configuration variables are case insensitive. The name of the variable resembles a path in a tree of configuration variables, with ``:`` character as segment separator. Since environment variables may not contain ``:`` character, the corresponding environment variable can be obtained by replacing them by **double** underscores (``__``), e.g. ``Emails:Port`` becomes ``Emails__Port``.

*******
General
*******

FrontendUrl
  Address where the web application is accessible. Used for generating links for emails.


******
Broker
******

Broker:Identity
  String identifier of the server used when communicating with workers. The identifier must be different from the one used by all w

Broker:ListeningAddress
  Address used for listening for workers. Must be in form ``tcp://[host]:[port]``. For example, to allow connections from the ``168.192.*.*`` subnet on port ``6000``, use ``tcp://168.192.0.0:6000``

Broker:TaskRetentionSeconds
  How many seconds to keep tasks for a certain game in a working queue when last worker who was capable of running given game disconnected. There is generally no need to change this setting.

Broker:HeartbeatConfig:HeartBeatInterval
  How many milliseconds between individual heartbeats between worker and broker.

Broker:HeartbeatConfig:Liveness
  How many heartbeats is a worker allowed to miss before being considered dead by the broker.

Broker:HeartbeatConfig:ReconnectIntervalInit
  How many milliseconds workers should wait before trying to reconnect to the broker for the first time after disconnecting.

Broker:HeartbeatConfig:ReconnectIntervalMax
  Upper bound for the exponential back off time for workers between reconnect attempts after disconnecting.

********
Security
********

Security:Key
  Symetric key used for creating JWT Bearer tokens for authentication.

Security:AccessTokenExpirationMinutes
  How many minutes should issued JWT access token be valid.

Security:RefreshTokenExpirationDays
  How many days should issued JWT refresh token be valid. Refresh tokens are used for requesting new access tokens and are invalidated on password change. After expiring, new tokens can be obtained by authenticating via email and p

Security:WorkerTokenExpirationMinutes
  How many minutes should access tokens issued to workers be valid. These tokens allow workers to download/upload files necessary for the task execution.

*******
Storage
*******

Storage:Directory
  Path to directory used as general file storage. Submissions, additional files and result files will be stored there.

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

*******
Serilog
*******

Used to configure the [Serilog](http://www.serilog.net) Logging library. See [official documentation](https://github.com/serilog/serilog-settings-configuration) for further details.
