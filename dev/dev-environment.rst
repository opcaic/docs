####################################
 Setting up development envrionment
####################################

The OPCAIC platform components can be developed both on Linux and Windows machines. We recommend
creating a directory dedicated only to the platform development, e.g. ``C:/opcaic`` on Windows
machines. In this directory, clone the respective sources::

  git clone https://github.com/opcaic/server
  git clone https://github.com/opcaic/web-app

******************************
 Server and worker components
******************************

The server and worker components share a single Visual Studio solution located at
``server/OPCAIC.sln``. The components can be started by an IDE like Visual Studio or using
commands::

  dotnet run --project src/OPCAIC.ApiService
  dotnet run --project src/OPCAIC.Worker

  
After starting up, the components will create more directories inside the ``opcaic`` directory, like
``server_storage`` ``worker_root``, which will be used to store files, and ``module``, which will be
searched for game modules.

.. note::

   When using the ``dotnet run`` command, the current directory for the Worker project will be set
   to current directory, not the directory containing, which will contain the ``OPCAIC.Worker.dll``,
   as it does in Visual Studio. This means that paths in Worker's ``appsettings.json`` need to
   modified (removing middle ``../../../`` segment) to achieve the same effect.

Development of these two components can be done independently of the web app
development. To interact with the server without using the web application, you can use `Swagger UI
<https://swagger.io/tools/swagger-ui/>`_ accessible by default on
``http://localhost:5000/api/swagger`` address.

Differences between development and production environment
==========================================================

ASP.Net applications by default distinguish multiple runtime environments. By default, the
application starts in ``Production`` environment. The environment can be changed by setting
``ASPNETCORE_ENVIRONMENT`` environment variable. The environment intended for local development is
``Develpment``, and the source code is configured to automatically set this environment when
starting the application using ``dotnet run`` command on the startup project or when starting the
application using an IDE, such as Visual Studio.

The development environment has relaxed requirements on the external services. It means that
e.g. email service is not used to send emails, instead the body of the emails is dumped in the log
stream and displayed on the applications standard output.

The database is also optional when developing locally. In the absence of
``ConnectionStrings:DataContext`` variable, the server uses `SQLite
<https://www.sqlite.org/index.html>`_ database in an in-memory mode to allow development. Upon
startup, the in-memory database is seeded with random data. However, it is highly recommended to
develop against real PostgreSQL database to eliminate possible differences in behavior between
development and production environments.

Setting up PostgreSQL database for development
----------------------------------------------

If you have PostgreSQL installed, all you need to do is set the ``ConnectionStrings:DataContext``
config variable.  To avoid committing local development configurations such as credentials to local
PostgreSQL database, development environment uses additional source of configuration called *user
secrets*. The configuration set via user secrets overrides the configuration set in environment
variables and ``appsettings.json``. To set the connection string for the application to use, run
following command inside the ``src/OPCAIC.ApiService`` folder ::

    dotnet user-secretes set "ConnectionStrings:DataContext" "Host=127.0.0.1; ..."
    
.. warning::

   The Secret Manager tool doesn't encrypt the stored secrets and shouldn't be treated as a trusted
   store. It's for development purposes only. The keys and values are stored in a JSON configuration
   file in the user profile directory.
   
.. tip::

   If you use Visual Studio, you can right-click on the project in Solution explorer window and
   click *Manage User Secrets* menu item to edit the stored secrets. For more information about user
   secrets, see `official documentation <https://docs.microsoft.com/en-us/aspnet/core/security/app-secrets>`_

Authentication
==============

Most of the endpoints require authentication via JWT token. The Swagger UI provides a way of setting
an Authentication header to be sent with every request. The basic workflow of accessing a protected
endpoint would be:

  - Making a POST request to ``api/users/login`` with (valid) user credentials, if the auto
    generated data are used, then ``Password`` is used as the password for all users.
  - saving the ``accessToken`` received from the response, and adding Authentication header with
    value ``Bearer {accessToken}``.
  - Accessing the protected endpoint as the authenticated user

However, the access token issued by the login endpoint has short expiration time, after the token is
expired, either new token must be requested by POSTing the ``refreshToken`` to ``api/users/{userId}/refresh``
endpoint or by reauthenticating using the ``api/users/login`` endpoint. To ease development, it is
recommended to change the expiration time of issued JWT tokens to sufficiently large number using
above mentioned user secrets mechanism::

    dotnet user-secrets set "Security:JWT:AccessTokenExpirationMinutes" 1000000

*******
Web app
*******

Starting the web application locally can be achieved by running following commands inside the source
code directory::

    npm install
    npm start

The second command starts a development server which monitors all source files and reacts to changes
by dynamically recompiling changed components and live-reloading them. There is therefore almost no
need to restart the server during development.

By default, the web application expects the ``server`` component to be running locally and listening
on the default ``http://localhost:5000`` address.

.. note::

   For technical reasons, when running local instance of server with in-memory SQLite database, all
   refresh tokens are invalidated when the server is restarted. This in effect means that user is
   logged out from the application and has to sign in again.
