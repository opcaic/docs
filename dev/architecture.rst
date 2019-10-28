#######################
 Architecture overview
#######################

The OPCAIC platform consists of several components:

- ``webapp`` - Modern React.JS-based web frontend application
- ``server`` - Application server written in ASP.NET Core 3.0
- ``worker`` - Worker application for distributed processing of to be used by the ``server``,
  written in .NET Core 3.0

These components can be developed/deployed independently. Additionally, the platforms requires a SQL
database (currently `PostgreSQL <https://www.postgresql.org>`_). The following diagram shows how the
individual components should interact.

.. todo:: Architecture diagram

The ``webapp`` repository resides in its own `GitHub repository
<https://github.com/opcaic/web-app>`_, ``server`` and ``worker`` components share a `single
repository <https://github.com/opcaic/server>`_ to simplify development.


**************************
 Running the code locally
**************************

Running the platform locally during development does not require any additional SW. Both server and
worker can be started directly from Visual Studio or other IDE, and webapp can be started using
``npm start`` command inside the repository. The ``server`` is able to run with an in-memory
database if no connection to PostgreSQL database is not configured. However, it is recommended to
run the server against real SQL database to avoid issues in production environment.
