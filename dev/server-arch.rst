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

The overall architecture of the server component follows the *clean architecture* practice. Projects
are grouped by purpose into several groups with clearly defined allowed dependencies. The groups are
listed below. Note that some of the projects are shared with the worker component.

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
    - OPCAIC.Broker (depends on OPCAIC.Messaging shared with worker)

:Persistence:
   Implements persistence of the domain objects into a database.

    - OPCAIC.Persistence

:Presentation:
   Exposes the application to it's consumers.

    - OPCAIC.ApiService

Figure :ref:`clean-arch-fig` illustrates the relationship between the parts of the architecture,
with arrows depicting allowed dependencies.

.. _clean-arch-fig:

.. figure:: img/clean-arch.svg
   :align: center
   :scale: 80%

   Structure and dependencies of projects in the server component.

Direction of the arrows is very important aspect of the clean architecture. For example:
``OPCAIC.Application`` project does not depend on the ``OPCAIC.Persistence`` project, even though
the application logic needs to communicate with database. This is achieved using *Dependency
Inversion* principle. The ``OPCAIC.Application`` project defines required functionality using C#
interfaces, and ``OPCAIC.Persistence`` provides implementation of these interfaces.

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

Figure :ref:`worker-arch-fig` puts the projects listed above into context, including shared
dependencies with the main server component.

.. _worker-arch-fig:

.. figure:: img/worker-arch.svg
   :align: center
   :scale: 50%

   Dependency diagram of worker component's projects
           
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

This small project contains cross-cutting concerns and definitions of ``EventId``\ s and tag names
for structured logging purposes.

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
since the new logic should be encapsulated in new request and handler classes.

The individual *handlers* for each use case are organized based on the entity on which operates, and
then categorized based on whether it is a *command* (request which modifies data) or *query*.

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

As we noted earlier, the ``OPCAIC.Persistence`` is refernces (is dependent) on the ``OPCAIC.Application``
project. The application project therefore defines interface for accessing the database and
persistence project provides the implementation.

However, The straightforward implementation of this idea could lead to many single-purpose methods
on the interface, like *GetTournamentsForUseCaseX*, *GetTournamentsForUseCaseY*, and adding new
functionality would ultimately require extending the said interface.

The above problem was solved using the *specification pattern*. The application defines
``ISpecification<TEntity>`` interfaces used to describe the query. The description includes:

    - filtering criteria on the database table
    - ordering specification (to get results sorted),
    - and offset and number of items to fetch (to support paginated requests)

The communication with database happens via ``IRepository<TEntity>`` interface which accepts the
specification objects. The underlying ``IRepositoryTEntity>`` implementation then uses the
information from specification object to query the database and return the results back to the
caller.

 There is also ``IProjectingSpecification<TEntity, TDestination>``, which is a variant of the
 ``ISpecification<TEntity>`` interface which adds projecting specification and allows for some
 transformation of the queried data, like fetching only subset of database columns.
 
This way, the details of database queries like filtering criteria still reside inside the
application project and there is no need to modify interfaces between application and persistence
projects when the query changes.


************
 Unit tests 
************

The solution contains comprehensive set of unit tests. Each project in the solution has a dedicated
test project under the ``test`` folder, with the exception of ``OCPAIC.Common``, which does not
contain any testable logic. The unit tests make heavy use of the `Moq
<https://github.com/moq/moq4>`_ library for mocking dependencies of the class under
test.

In addition to regular unit tests which concentrate on functionality of a single class, there is the
``OPCAIC.FunctionalTest`` project. Tests in this project are targeted on the server as a
whole. These tests start the server and test it's functionalit by sending HTTP requests analyzing
the server's responses.
