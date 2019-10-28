################################
 Server components architecture
################################

The source code is organized into several projects with clearly defined purpose in order to keep the
architecture clean and easily changeable.


*******************
 Solution overview
*******************

The server repository holds a single solution which contains source code for both server and worker
components, and the communication layer between those two components.

Server component
================

The overall architecture of the server component is divided into following parts, with listing of
the source code projects which belong to it. Some projects contain logic that is shared with the
worker component.

:Domain:
   Defines types and classes which are used throughout the server component.

    - OPCAIC.Domain
    - OPCAIC.Common (Also shared with worker)

:Application:
   Contains all application specific logic.

    - OPCAIC.Application

:Infrastructure:
   Implements communication services outisde of the application scope (sending emails).

    - OPCAIC.Infrastructure
    - OPCAIC.Broker

:Persistence:
   Implements persistence of the domain objects into a database.

    - OPCAIC.Persistence

:Presentation:
   Exposes the application to it's consumers.

    - OPCAIC.ApiService

Following image illustrates the relationship between the parts, with arrows depicting dependencies
between them.

.. todo::
   Clean architecture image, concentric rings, from inside: Core, application, (persistence,
   infrastructure, presentation)

The important part is the direction of the arrows. For example: ``OPCAIC.Application`` project does
not depend on the ``OPCAIC.Persistence`` project, even though the application logic needs to
communicate with database. This is achieved using *Dependency Inversion*. The ``OPCAIC.Application``
project defines (via C# interfaces) what logic it needs from the database, and
``OPCAIC.Persistence`` provides implementation of these interfaces.

Worker component
================

Instances of the worker component create a pool of machines which are used for evaluating
(potentially long running) tournament matches. The backend implementation is again separated to
multiple projects.

:Worker:
   Implementation of the Application logic to be executed on individual machines

   - OPCAIC.Worker
   - OPCAIC.GameModules.Interface

:Broker:
   Deployed as part of the server, manages worker pool, load balancing and dispatching of tasks to
   individual workers.

   - OPCAIC.Broker

:Communication Layer:
   Implements communication between Worker and Broker projects.

   - OPCAIC.Messaging

Following image puts the projects listed above into context, including shared dependencies with the
main server component.

.. todo::
   Worker projects with arrows to the main server components

Following sections will describe these projects in more details.
   

*******************
 Server component
*******************

As outlined in the previous section, the architecture of the server is divided into projects based
on the code's responsibility. This section gives more detailed information about the inner designs
of the code structures used in individual projects

OPCAIC.Domain
=============

This project contains enums and classes which describe the individual entities in the domain. By
design, this project does not contain any application specific logic, or any logic concerning
persistence or serialization of the entities. Also, this project contains ``Enumeration`` and
``ValueObject`` classes to be used throughout the project.


Enumerations
------------

In some cases, simple lanugage provided ``enum``\s are not appropriate, for example if enums are
used for a fixed list in a dropdown menu, simple changes like adding a new item require recompiling
and redeploying. In case the project does periodical releases with multiple staging environments,
such "simple change" may take weeks to get to production.

Inspired by many blog posts on why using ``enum``\s is not alwasy optimal (e.g. `Enums are Evil by
Thomas Weingartner <https://www.planetgeek.ch/2009/07/01/enums-are-evil/>`_), we implemented the
concept os *smart enum*, which not only is extensible during runtime (e.g. by loading members from
file or database). Simple example can be found in the ``GameType``, which provides additional
information about the game type, like what tournament format does the type support. Another example
is the ``EmailType`` members of which can be also used as a factory for email data structures.

Value objects
-------------

Concept of value objects is taken from *Domain Drive Design*. A *value object* represents an entity
whose equality is based on the equality of it's individual components. E.g. Two addresses are equal
if all its components (street name, city, ZIP code...). To make the implementation of such objects
easier, a ``ValueObject`` base class was adapted from the Microsoft's blog post `Implementing Value
Objects
<https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/implement-value-objects>`_. This
base class requires implementing only the ``GetAtomicValues()`` method to get its individual
components. This also automatically works with inheritance hierarchies. For example, see
``MenuItem`` class.

OPCAIC.Common
=============

This small project contains cross-cutting concerns and definitions of ``EventId``\s and tag names
for logging purposes.

.. todo:: logging link in paragraph above

OPCAIC.Persistence
==================

This project encapsulates communication with database and how entities defined in ``OPCAIC.Domain``
are mapped to database tables. This project uses `Entity Framework Core
<https://docs.microsoft.com/en-us/ef/>`_, which is an Object-Relational Mapper (ORM) library. This
library encapsulates differences between individual (not only) SQL databases.
          
OPCAIC.Infrastructure
=====================

This project implements communication with services outside of the application. Currently, there is
only logic concerning sending email notifications.


OPCAIC.Application
==================

This object contains main application logic. Instead of more traditional *N-tier* architecture, this
project uses so called *Vertical slices* architecture. Instead of encapsulating logic into layers
like *service layer* and *database layer*, vertical slices encapuslates code based on it's *business
use-case*. For example, there is a ``CreateTournamentCommand`` class which represents a request to
create a new tournament. then there is a corresponding ``CreateTournamentCommand.Handler`` class
wich is able to carry out this request and encapsulates all needed logic.

In *Vertical Slices Architecture*, adding a new feature should not require modifying existing code,
since the new logic should be encapsulated in the new use case. The individual *handlers* for each
use case are organized based on the entity on which operates, and then categorized based on whether
it is a *command* (request which modifies data) or *query*.

MediatR
-------

The application project makes heavy use of the `MediatR <https://github.com/jbogard/MediatR>`_
library, which implements automatic discovery of request handlers and dispatch of request objects to
them. This makes the coupling very loose between the handlers and the code that needs the logic they
provide.

AutoMapper
----------

Another library which is heavily used in the project is `AutoMapper
<https://github.com/AutoMapper/AutoMapper>`_. This library simplifies mapping between two
objects. When using automapper, there is no need to manually list all properties which need to be
copied from one instance to the other and risk forgetting to update some code when a new property is
added to a type.

Mappings between types have to be specified beforehand in order to be compiled. This is both for
performance reasons and protecting against unintended mappings. However, having a central file where
these mappings are listed is not optimal, because the mapping is not visible when looking at class
definition. Also the centralized solution fails when one of the classes is not visible due to the
directions of dependencies between projects. To resolve the situation, two empty interfaces
``IMapTo<TDestination>`` and ``IMapFrom<TSource>`` can be implemented to mark that a map should be
created between given types. If the mapping requires special configuration, interface
``ICustomMapping`` can be used to specify any mapping in its ``CreateMapping`` method. These
interfaces are then examined on startup and appropriate mappings created in the
``AutoMapperProfile`` class.

Database query specifications
-----------------------------

Because the ``OPCAIC.Persistence`` is dependent on the ``OPCAIC.Application`` project, it is not
possible (nor desirable) to the logic directly. To make the direction of dependency work, the
application project defines interfaces which are then implemented in the persistence
project. However, this could lead to some very specialized methods on the given interface to be used
only by a particular use-case handler.

To avoid this, there are ``ISpecification<TEntity>`` objects which encapsulate queries for obtaining
entities from database. On these specifications, it is possible to specify filtering, ordering and
other criterias in the form of ``Expression<Fun<TEntity,...>>`` types. There is also
``IProjectingSpecification<TEntity, TDestination>``, which adds projecting capabilities to query to
allow selecting only parts of the object. This way, the details of database queries are still stored
inside the application project and there is no need to modify interfaces between application and
persistence projects when the query changes.
