.. _security:

##########
 Security
##########

This chapter summarizes design and implementation of security related concerns throughout the application.


**************
Authentication
**************

Our application uses `ASP.NET Core Identity
<https://docs.microsoft.com/en-us/aspnet/core/security/authentication/identity>`_ library for
implementing user management. The library securely implements password hashing handles credentials
authentication. The library supports many advanced features currenlty not used by the platform, such
as external login providers, such as Facebook or Google accounts, account lockout or Two-Factor
authentication. These features can be utilized in future development.

Once user is logged in, authentication is done using `JWT (Json Web Token) <https://jwt.io>`_
mechanism to establish identity of the client communicating with the server. Upon login, user
receives two tokens: *access token* and *refresh token*. The access token is to be passed in the
HTTP Authorization header on each request, and is valid only for certain period of time
(configurable by the ``Security:JWT:AccessTokenExpirationMinutes`` config variable on the server).

After the access token expires, the client needs to request a new token using the refresh
token. The refresh token embeds a stamp that is checked with the the user record in database, if
stamps match, then new pair of access and refresh tokens are issued. Security critical operations
like password change/reset invalidate the refresh tokens by changing the user's security stamp in
the database, causing the above described validation to fail.


*************
Authorization
*************

Once the identity of the user is established the user's permissions are checked before processing
the request. The platform internally defines a set of permissions, these are of two categories

Resource-based permissions
  Permissions to operations on particular resource. Permissions such as to upload a submission to
  particular tournament belong to this category

General permissions
  These permissions are not related to a particular resource. Examples include permissions to
  operations such as creating a new game.

Permissions are organized by the entity type on which the protected opration operates and
are represented as ``enums`` in the source code, for example ``TournamentPermission`` enum contains a
list of permissions regarding all operations on tournament entities, like Create/Read/Update/Delete
permissions.

The mapping of which users has which permissions on which resource is rule-based. The decision to
authorize an operation is generally done with regards to:

    - User role - admin, organizer, user or none (not logged in)
    - Parent tournament entity, if the resource is e.g. match or submission

        - being an owner or manager,
        - Visibility settings of the tournament

    - Author/ownership of the resource

Users with the admin role have implicitly all permissions in the platform, rules determining
permissions of other users are grouped by the entity type in classes such as
``TournamentPermissionHandler``. The platform contains a unit test that explicitly tests that all
permission types have a rule in the corresponding handler.


************************
Communication Encryption
************************

The server component **does not** implement any communication encryption when communicating with
clients, nor enforces HSTS or other security mechanism. The reason for that is that the server is
expected to be hosted behind a *reverse proxy* and receive only requests forwarded by the
proxy. SSL encryption of the communication can be then provided by the reverse proxy.

This arrangement allows the backend to use unencrypted communication between server and
worker. These components are expected to be connected in an otherwise isolated LAN network and thus
no communication encryption is supported.


******************************
Protection against DoS attacks
******************************

The server component implements only limited protection against DoS (Denial of service) attacks by
using the `AspNetCoreRateLimit <https://github.com/stefanprodan/AspNetCoreRateLimit>`_ library. This
library is able to do rule-based filtering based on the IP of the client and limiting specification
on the endpoints and automatically adds standard response headers such as *Retry-After*. All
configuration of the library is done via configuration variables, list of which can be found at
:ref:`request-limiting-config`.

If level of protection provided by the above mentioned library is not sufficient, then additional
measures are expected to be provided at the level of reverse proxy.
