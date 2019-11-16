################################
 Admin documentation
################################

******
Basics
******

Availability
============

Apart from the public part of the web, there is also an administration part (module), which provides
support for managing tournaments, games and users in system and basic monitoring and maintenance of
application.  This module is only accessible to users which were granted a sufficient role -
organizer or admin. If the user does not have one of these roles, he sees only "forbidden" error
page.  Normal users can be promoted to both of these roles by admins.

Features
========

The administration module is divided into several submodules. Not all of the submodules are
available to both organizers and admins, as the organizers are not meant to manage the application
itself, and thus cannot have access to all of the admininstration features. The submodules are:

    - Dashboard 
    - Tournaments
    - Games
    - Users
    - Email templates
    - System

Roles
=====

The first of these roles is *organizer*. As the name suggests, these are users who are meant to
conduct the tournaments.  They are granted access to submodules which serve for that purpose and not
to anything else regarding the administration of the application itself.  Specifically, the
following submodules are available to them:

    - Dashboard
    - Tournaments
    - Games

The second role is *admin*. This role is supposed to suit for administrating the whole application,
so all of the submodules are available to these users.  There are few submodules (the ones which are
available to organizers as well) which manage current games and tournaments of the platform and also
submodules intended to serve for administrating the application itself, that is for example managing
its users, work currently being processed on the server and so on.

Getting to admininstration module
=================================

The admininstration module can be reached by clicking on the tab Administration on the main page.
All submodules are reachable from sidebar on the left side. On the bottom of this sidebar there is a
link which leads back to root page of public module.

***********************
 Administration module
***********************

General 
=========

There are two views on entities in this module: table view and detail view.
    
Table contains preview of data – only main attributes, by which these entities can be differentiated. 
Table uses pagination – fetching and viewing of data, which follows, so that not all data are fetched at once. Pagination is specified on the bottom of table. Items are fetched according to filter and sort, which are specified in header of table - sort order is changed after click on name of sortable column and always is one of *none*, *ascending*, and *descending*, filter can be specified after click on magnifying glass (search) or funnel (choice). Lists are asynchronously reloaded after each change of filter, sort or pagination, so there is no need for any "refresh" button.

After click on “Detail” button in row of particular entity the detail view of this entity is shown. On this view there are all data about explored entity, usually as form, by which these data can be edited. All actions available on entity are also reachable from this view.

Dashboard
=========

The first submodule of the administration part of the web, and the landing page of it, is the *Dashboard* submodule. This submodule is available to both organizers and admins (with the exception of one sub-table).
It shows the most important information about whats going on on the platform regarding the user and also serves as a 'crossroad' of links to different detailed pages in the administration module.

Recent tournaments
------------------

First table shows *recent tournaments* - for organizers, only the ones they have the manager rights to, for admins, any recent tournaments. Each tournament has its basic properties listed in table, along with a *Detail*
button, leading to tournament's administration detail page. This page is descripted in the subsection Tournaments - Tournament detail.

Failed matches
--------------

This table shows a list of matches in tournaments organized by the user, whose execution failed. The basic information about each match is given, and there is also a *Detail* button, leading to the specific matches detail page,
as described in the following sections.

Failed and invalid submissions
------------------------------

Following two tables shows lists of submissions that were not validated correctly. The difference between Failed and Invalid submissions tables is that in the Failed submissions table, there are submission for which the validation failed because of some error in system, for example due to non-existence of game module, which validates game of submission. Submission is considered as invalid and shown in second table if submission validation failed because of mistake by user, who submitted it, for example when some files are missing or cannot be compiled. 

Both the tables show submissions' *Date*, *User*, *State* and the *Tournament* they were submitted to. For each of them, there is also a detail button, leading to submission detail page, as described in the following sections. 

Games without implemented module
--------------------------------

The last table of the Dashboard module is available only to admins. It shows a list of games, which does not have a game module implemented. System admins should secure that this table is empty by implementing game modules for all created games. 

Tournaments
===========

The second is the *Tournament* submodule, which provides functionality to manage tournaments running
on the platform. This part of the administration is available both to organizers and admins.

Creating a tournament
---------------------

On the top of the page, there is a *Create new tournament* button, which redirects to a form used to
that matter.  The form has both mandatory and optional fields, where the optional fields are usually
prefilled with some default values.

In the first part of the form, the user has to specify the *Name* and the *Game* of the
tournament. If the game chosen has a custom configuration (more on that in the Games section),
another part of the form will appear, containing game configuration. These values can be
changed accordingly to the schema of the game.

Availability of the tournament is subject of the second part of the form. It's possible to specify
the whole tournament's *availability* - public (when users can join without explicit invitation) or private (invitation sent through participants module is needed for joining tournament), as well as the *visibility of its match
logs*.  The tournament can also by *anonymized*, which means that the users of the tournament will
be presented on the tournament's page under anonymous nicknames generated by the app.

The next part specifies tournament's basic properties, that is its *scope*, *format* and *ranking
strategy*. Not all combinations of scope and format are allowed. When scope of tournament is selected, only available formats are shown. When scope *deadline* is selected, date and time of deadline has to be picked from picker. Otherwise, when tournament should have *ongoing* scope, user have to enter number of matches, that will be played each day. The *size of the submissions* can be limited through following field, minimal possible limit is 1MB.

The last two parts handle the tournament's detail page. Organizer of a tournament can choose either
*game design* (meaning that the page will use game's default design), or he can *specify his own
design* by choosing a title image and theme color for the tournament's page. Finally, tournament's
description can be written in a text box on the bottom of the form. The text box supports markdown
formatting, and the user can preview the final look of the text.

Tournaments list
----------------

The main part features a table with a list of tournaments to manage - for organizers there are only
tournaments they own or have manager rights to, while the admins see all the tournaments.

The table displays basic properties of each tournament, that is its name, game, when it was created,
whether it's published, its state, format and scope, and optionally also the deadline.  In the last
two columns, there are also two buttons, *Clone* and *Detail*

The *Clone* button suits for copying a tournament - it leads to a *Create new tournament* form,
prefilled with values copied from the original tournament.  *Detail* button redirects to admin
section Tournament detail page, which is decribed in the next section.

This part of the administration is available both to organizers and admins

Tournaments detail
------------------

Administration tournament's detail page serves for managing the tournament itself. It contains
several tabs.

First tab is *Basic info*. A small table with number of *participating players, submissions, all
submissions* and tournament *state* can be seen on the top of the page.  Depending on the tournament
state, there are different control buttons in the right top part. These buttons serve for changing
tournament's state:

    - Publish - make the tournament available for users
    - Start - start the evaluation
    - Pause/Unpause - pause/unpause the evaluation
    - Stop (for ongoing tournaments) - end the tournament

In the central part, there is a same form as on the Create new tournament page, where organizers can
edit the tournament's properties.  For tournaments in the state created, almost all of the
properties can be further edited (apart from game of the tournament), while for published
tournaments, some properties are immutable in order to mantain correct working of the app.  On the
very bottom of the page, there is a table with *Menu items*. These menu items are shown on the left
sidebar of the tournament detail on the public part of the web.  New items can be added through
dedicated button. There are two types of menu items. First one is an *External menu item* - a named
link to a web page outside OPCAIC.  Second type is a *Document menu item*, and it's basically a
named link to a document created on the *Documents* tab, which is described in the following
section.  Finally, there is a *Save* button to save the edited tournament.

*Documents* is a tab for managing tournament documents, describing for example game's rules, API and
so on.  All of the tournament's documents are listed there, with *Detail* buttons leading to their
detail pages. There is also *Create new document* button, leading to a new document detail page.
The detail page of document features field for specifying the tournament's name, and there is also a
text box with the contents of the document.  The text box supports markdown formatting, and the
preview of the formatted text can be seen by clicking the appropriate button.

Next tab is called *Managers*, and it serves for making other users managers of the tournament. Only owners and system admins can add  other users with role organizer by choosing their email from the listbox. These users can be also deleted from the list by clicking the *Delete* button. As manager of tournament, user can view all data and perform actions on this tournament, except for adding another managers and deleting tournament and its additional files.

Through the *Participants* tab, you can invite people to join your tournament. This is intended
mainly for private tournaments, as they cannot be seen otherwise. Anyone can be added, even someone
who is not a user of the platform, by writing down their email. An invitation mail will be sent to
the given addresses, together with a link to the tournament. People who do not have the account yet
will have to register first (with the specified email) to be able to join the tournament.

*Matches* tab serves for managing tournament's matches. All matches are listed here in a table,
together with some basic information about the match's execution. These information are: *queue
time, execution time, players and theirs score* and also match's *state*. In the last two columns,
there are also two buttons. *Queue rematch execution* serves for forcing app to try to execute the
match again. This button is available only for matches in state Failed. Button *Detail* leads to
matches detail page. On the detail page, there is there is a list with one or two tables (depending
on match's state) for each of the executions. First table is *Basic info*, and it shows *id* of the
match, its *job id* (more on that in the System submodule section), dates of *creation* and
*execution*, *players* with links to their *submissions*, and the result of the execution along with
its log (shown by clicking the button *Show log*). If the match was executed succesfully. If the
result of execution is successful, there is also a button *Download additional files* along with a
second table, *Players data*, which shows detailed results of the match. The values of the fields in
this table are game dependent, except for the field *score*, which determines the match's
result. Button *Download additional files* serves for downloading all files produced by game when
executing the match. The number and meaning of these files is again game dependent, except for the
file *match-results.json*, which contains the source data for *Players data* table.

Next tab of the tournament's detail is called *Submissions*. It shows a table with all of the
tournamenet's submissions, along with their *Date*, *User*, *State*, flag showing whether they are
*Active* in the tournament, and a button *Detail* leading to their detail page. On the detail page,
there a few tables similar to these on the match's detail page. First one is *Basic info*, and it
shows the same fields as seen in the table on the main Submissions tab. Then, there are two
buttons. *Download submission* is self-explanatory, and the *Run validation again* forces app to try
to validate the submission again. Under these buttons, there is a list of all submission's
validations, along with their *date*, *checker*, *compiler* and *executor* result (along with the
appropriate logs) and optionally *Exception* field, if something went wrong during the
validation. Lastly, there is also a list *Played matches*, showing the same table as on the matches
tab, just filtered by the currently shown submission.

*Leaderboard*, the last tab, shows only just the leaderboard of the tournament, as seen in the
public part of the web.

Games
=====

*Games* tab serves for managing games on the platform. This submodule is available to both
organizers and admins.

Creating a game
---------------

On the top of the page, there is a *Create new game* button, leading to a page with a form for
filling the game information. The first three fields are mandatory, that is game's *Name*, *Key*
(specifies game module, which will be used for validating submissions and executing matches) and the
*Type* of the game - either single player or two players game. Then, there is a part which suits for
picking game public page design. Game's *logo*, *tournament default logo* and the default
*tournament color* can be chosen. User can also specify size limit of additional game files for the
tournaments to be played. Finally, the text box *Description* contains description of the game, and
supports markdown formatting, same as other text boxes mentioned in previous sections.

Games list
----------

Table with a list of all created games fills the central part of the page. Note that *created* game
does not mean it has got an appropriate game module and thus for these games, no matches can be
executed. The table contains columns with few basic game properties, such as *Name*, *Key*
(specifying the module used for the game) and the *Number of active tournaments*. There is also a
*Detail* button in the last column of the table, leading to the game's administration detail page.

Game detail
-----------

The administration game detail page contains two tabs, *Basic info* and *Configuration*. Basic info
serves for viewing/editing the game, and it shows a same form as on the *Create new game* page,
prefilled with game's information. The second tab, *Configuration* allows to specify the format of
game configuration file, which will be needed to execute the matches. The game configuration may
specify for example timeout for bot's turns, initial resources and so on, depending on the specific
game. The format of the configuration file is determined by a JSONSchema (see
https://json-schema.org/understanding-json-schema/), which the admin has to write in the *Schema of
configuration* box. After filling this window, a *Sample form* for specifying a configuration
following the given schema will be shown in the left part of the page. There are quite a few web
tools which can be used to create a JSONSchema from an example Json file, for example
https://jsonschema.net/. Specifying game configuration schema obviously makes sense only in case the
organizer knows how the specific game module works, so that it uses it correctly.

Users
=====

Next module serves for managing platform's *users* is available solely for admins. 

Users list
----------

The submodule's main page again shows a list, this time the list of all users on the platform. Each
user has a few basic characteristics shown there, such as *Username*, *Email*, *Role* and the *Date
of creation*. Last column again contains button *Detail* leading to users' detail page.

User detail
-----------

User detail page serves for managing the individual users. The *username* and the *email* cannot be
edited. For the email, information about whether the email is verified or not is shown. The *role*
of the user (user, organizer or admin) can be changed, and also the *organization*, which the user
belongs to can be specified. It's also possible to enable or disable *email notifications* for the
user.

Email templates
===============

Using *Email templates* submodule, admins can edit the templates for the emails send to users at
various occasions, such as verifying of the email, resetting password and so on.

Templates list
--------------

The main table shows a list of email templates, their *name* and *localization* (language of the
template) and *Edit* button, leading to the *Edit template* page.

Edit template
-------------

On the edit template page, there is a form defining the email template. Some of the properties are
immutable - that is the *name*, *localization* and the *variables* of the template. Appropriate
values are substituted into the variables when sending the email. For example, for ResetPassword
template, the ResetURL is a variable, filled with the appropriate link when sent to the user.

The *subject* and the *body* of the template can be edited. For the body, html can be used. The
*preview* window then displays preview of the final template.

System
======

Submodule *system* is used for 'low level' administration of the platform, such as managing current
processes - 'jobs', being executed on the servers. It's thus available only to admins.

Workers
-------

The table *Workers* shows a list of current 'workers' - machines which run the validations and
executions. Each worker has an entry in the table specifying the worker's *identity* (unique name),
*current job id* (id of the job currently being processed on the machine) and *available games*
(keys of implemented game modules).

Work items
----------

The table *Work items* serves for managing the actual jobs planned on the workers. It shows a queue
of currently planned jobs. For each of those jobs, the table shows its *id*, *game* and *how long it
is queued*. Then, there are two control buttons. *Prirotize* serves for prioritizing the job in the
queue, so that it will be processed earlier than other jobs queued. The other button, *Cancel*,
cancels the job (removes it from the queue).

*******************
Diagnosing problems
*******************

Flawless execution of tournaments requires flawless inputs from multiple users of the platform and
there are several stages of the tournament lifetime which are prone to human errors. This section
provides a guide on how to diagnose and subsequently repair common errors when using the OPCAIC
platform.

Searching the log files
=======================

In case the problem is not evident from diagnostics visible in the administration section of the web
application, additional information can be retrieved from logs generated by the platform. Since the
platform backend is composed of multiple processes running potentially on different machines, we
reccommend installing Graylog alongside the platform for log aggregation and efficient log
searching. For installation instructions see :ref:`graylog-installation`.

The platform backend utilizes structured logging. Meaning that alongside regular log messages, all
messages are annotated with structured contextual data. It means e.g. that each log message produced
while processing a user request is annotated with a user id, username, email; each log message
regarding to some tournament will be annotated by the tournament id etc.

.. note::

   In default configuration, standard output of the server processes does not dump all variables
   listed below. The format of printed log messages can be configured in ``appsettings.json`` by
   adding an ``outputTemplate`` option to the console sink. See `Serilog github website
   <https://github.com/serilog/serilog-settings-configuration>`_ for more details.

Following sections list the most useful variables grouped by topic.

General variables
-----------------

StatusCode
  Status code returned from http request on the server's web API.

RequestPath
  Path part of the requests URL.
  
HttpRequestMethod
  HTTP method of the request.

ElapsedMilliseconds
  Time spent processing given request in milliseconds. 


User information
----------------
  
UserId
  Id of the author of the request.

UserEmail
  Email of the author of the request.

Username
  Id of the author of the request.

UserRole
  Id of the author of the request.


Ids of the relevant entities
----------------------------
 
In administration section of the web application, it is possible to see the unique ids of the
individual entities. These can used to filter out desired logs.

JobId
  Uniquely identifies a task dispatched to worker for execution. The task can be either submission
  validation or match execution.

SubmissionId
  Id of the user submission.

MatchId
  Id of the match.

ExecutionId
  Id of the match execution.

ValidationId
  Id of the submission validation.

TournamentId
  Id of the tournament.

TournamentState
  State of the tournament.

GameId
  Id of the game.


Task execution on a worker
--------------------------

Game
  Name of the game module servicing the match execution or submission validation. This corresponds
  to the game key from the game administration screen.
  
EntryPoint
  Name of the entry point being executed.
  
GameModuleProcessExitCode
  Exit code of the game module process.
  
GameModulePID
  Process ID of the game module process.
