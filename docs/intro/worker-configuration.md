# Worker configuration

The worker component uses several configuration variables which can be used to customize the platform behavior. Variables can be set by command line parameters, `appsettings.json` configuration file or environment variables. The environment variables take precedence over the configuration file and command line parameters take precedence over environment variables.

Names of the configuration variables are case insensitive. The name of the variable resembles a path in a tree of configuration variables, with `:` character as segment separator. Since environment variables may not contain `:` character, the corresponding environment variable can be obtained by replacing them by **double** underscores (`__`), e.g. `Emails:Port` becomes `Emails__Port`.

## General

| Name         | Description                                    |
|--------------|------------------------------------------------|
| `ModulePath` | Path to the directory containing game modules. |

## Connector configuration

Configuration of the connection to the server.

| Name                            | Description                                                                                                                            |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `ConnectorConfig:Identity`      | Identity string used for communicating with the server. Must be different to the identities of other workers and to that of the broker |
| `ConnectorConfig:BrokerAddress` | Address on which the server listens for workers. Must be in form `tcp://[host]:[port]`.                                                |

## File server

Configuration of where to download additional files from and where to store result files.

| Name                       | Description                                                                                                                                                       |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FileServer:ServerAddress` | Base address for the file storage server. Currently, the file server is part of the main server, so the address must be `http://[server-host]:[server-port]/api/` |

## Task execution configuration

Configuration related to the performing submission validations and match executions.

| Name                              | Description                                                                                                                                                                                                                                                           |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Execution:WorkingDirectoryRoot`  | Root directory where temporary files of currently executed job will be stored.                                                                                                                                                                                        |
| `Execution:ArchiveDirectoryRoot`  | Root directory where temporary files of finished jobs will be stored for diagnostic purposes. Note that the platform does not provide automatic deletion of old directories, so make sure that old  directories are deleted regularly to prevent disk space shortage. |
| `Execution:MaxTaskTimeoutSeconds` | Global upper limit on the duration of any task (submission validation or match execution). Game modules should take care of task-specific timeouts. This setting should be used to protect worker against game module freezes.                                        |

## Serilog

Used to configure the [Serilog](http://www.serilog.net) Logging library. See [official documentation](https://github.com/serilog/serilog-settings-configuration) for further details.
