.. _worker-configuration:

####################
Worker configuration
####################

The worker component uses several configuration variables which can be used to customize the
platform behavior. Variables can be set by command line parameters, ``appsettings.json``
configuration file or environment variables. The environment variables take precedence over the
configuration file and command line parameters take precedence over environment variables.

Names of the configuration variables are case insensitive. The name of the variable resembles a path
in a tree of configuration variables, with ``:`` character as segment separator. Since environment
variables may not contain ``:`` character, the corresponding environment variable can be obtained by
replacing them by **double** underscores (``__``), e.g. ``Emails:Port`` becomes ``Emails__Port``.

.. note::

   To apply changes made in ``appsettings.json`` file, the worker process needs to be restarted.

*******
General
*******

ModulePath
  Path to the directory containing game modules.

  
***********************
Connector configuration
***********************

Configuration of the connection to the server.

ConnectorConfig:Identity
  Identity string used for communicating with the server. Must be different to the identities of
  other workers and to that of the broker.

ConnectorConfig:BrokerAddress
  Address on which the server listens for workers. Must be in form ``tcp://[host]:[port]``.


***********
File server
***********

Configuration of where to download additional files from and where to store result files.

FileServer:ServerAddress
  Base address for the file storage server. Currently, the file server is part of the main server,
  so the address must be ``http://[server-host]:[server-port]/api/``


****************************
Task execution configuration
****************************

Configuration related to the performing submission validations and match executions.

Execution:WorkingDirectory
  Root directory where temporary files of currently executed job will be stored.

Execution:ArchiveDirectory
  Root directory where all files generated during execution of successfull tasks will be stored for diagnostic
  purposes.

Execution:ArchiveRetentionDays
  How many days should files in the archive directory be kept. default is 30 days.

Execution:ErrorDirectory
  Root directory where all files generated during execution of failed tasks will be stored for diagnostic
  purposes.

Execution:ErrorRetentionDays
  How many days should files in the error directory be kept. default is 30 days.

Execution:MaxTaskTimeoutSeconds
  Global upper limit on the duration of any task (submission validation or match execution). Game
  modules should take care of task-specific timeouts. This setting should be used to protect worker
  against game module freezes. It is expected that each game module will keep it's own timeout
  specific to the particular game. Default value is 300 seconds (5 minutes).

  
*******
Serilog
*******

Used to configure the `Serilog <http://www.serilog.net>`_ Logging library. See `official
documentation <https://github.com/serilog/serilog-settings-configuration>`_ for further details.
