.. _adding-new-games:

########################################
Adding a new game module to the platform
########################################

Adding a new game consists of following 3 steps:

1) Creating a game module for the new game
2) Deploying the newly created game module
3) Configuring the new game in the administration section

The second and third steps can be done only by platform administrators (users with *admin* role), as
it requires access to both the machine where worker components are hosted and access to
administration section inside the web application.

**************************
 Creating the game module
**************************

From the OPCAIC platform's perspective, a *game module* is a black box component with a set of
defined entry points for invoking actions like validating whether given submission is correct (can
participate in a tournament) or executing a match between submissions.

Required entry points
=====================

There are total 5 entry points: *checker*, *compiler*, *validator*, *executor* and *cleanup*. These
are combined into two pipelines:

* *Validation pipeline*: invoked to validate newly submitted solution to game's tournament

  - checker
  - compiler
  - validator
  - cleanup

* *Execution pipeline* : invoked to execute individual matches between submissions

  - compiler - invoked for all submissions separately
  - executor
  - cleanup

Checker entry point
-------------------

Checks that the submission submitted by the user contains all the files needed. This step is there
explicitly to be able to provide meaningful error messages to users when there is something wrong
with the submission.

:Arguments:
   - Path to additional files directory (specific for given tournament).
   - Path to the directory with submission files.
:Exit codes:
   - 0 - Submission is correct and may proceed to the next stage
   - 200 - There is a problem with user's submission (user's fault)
   - other - General error (module's fault)

Compiler entry point
--------------------

Compile the submission files to a form which executor can accept. The most prominent example is
compiling the submission files into an executable.

:Arguments:
   - Path to additional files directory (specific for given tournament).
   - Path to the directory with submission files.
   - Path to the output directory where results of the compilation should be stored.
:Exit codes:
   - 0 - Compilation was successful
   - 200 - Submission cannot be compiled (user's fault)
   - other - General error (module's fault)

Validator entry point
---------------------

Smoke tests the compiled submission, e.g. execute a testing match between to check that it does not
crash.

:Arguments:
   - Path to additional files directory (specific for given tournament).
   - Path to the directory with compiled submission (output directory from the compiler entry point)
:Exit codes:
   - 0 - Submission is valid and may participate in the tournament
   - 200 - Submission is considered invalid (user's fault)
   - other - General error (module's fault)

Executor entry point
--------------------

Executes a match between submissions.

:Arguments:
   - Path to additional files directory (specific for given tournament).
   - [1 - N] Paths to directorys with compiled submissions (products of the compile entry point)
   - Path to directory where additional output can be stored
:Exit codes:
   - 0 - Match executed successfully
   - other - General error (module's fault)

Additionally, the executor entry point must store match results in a ``match-results.json`` file
inside the provided output directory. The output must have an array property 'results' containing
objects with numeric 'score' property This property is used to determine the relative ordering
between the submissions which participated in the match (and hence the winner). The result file can
contain also additional statistics from the match. Example ``match-results.json`` file contents can
be seen below:

.. code-block:: js
   :caption: Example *match-results.json* file produced by the executor entry point.

    { 
        'results': [
            {
                'score' : 0,
                'hitRate': 0.7
            },
            {
                'score' : 1,
                'hitRate': 0.82
            }
        ],
        'totalSeconds': 59.4,
        'totalShots': 64
    }

The values of the *score* property can be arbitrary numbers representable by 64-bit floating point
number. The only requirement is that the scores produced be different for the individual bots to
always assure clear winner.

Cleanup entry point
-------------------

Performs cleanup of resources not controlled by the platform. For example killing hanging process of
a game after failed match execution

:Arguments:
   - Path to additional files directory (specific for given tournament).
:Exit codes:
   - 0 - Success
   - other - General error (module's fault)

Specifying the entry points
===========================

Commands for individual entry points are specified in ``entrypoints.json`` file which should be
located in module directory. Example file contents follow:

.. code-block:: js
   :caption: Example *entrypoins.json* file contents for specifying game module's entry points

    {
        "Checker": {
            "Executable": "python",
            "Arguments": [
                "./scripts/check.py"
            ]
        },
        "Compiler": {
            "Executable": "python",
            "Arguments": [
                "./scripts/compile.py"
            ]
        },
        "Validator": {
            "Executable": "dotnet",
            "Arguments": [
                "Game.dll",
                "execute",
                "--test",
                "--no-output"
            ]
        },
        "Executor": {
            "Executable": "dotnet",
            "Arguments": [
                "Game.dll",
                "execute"
            ]
        },
        "Cleanup": {
            "Executable": "bash",
            "Arguments": [
                "./scripts/cleanup.sh"
            ]
        }
    }

The ``Executable`` field should contain the name or path to the program to be executed, The
``Arguments`` field is an array of command line arguments which are passed to the executable. The
arguments specified in ``Arguments`` are put *before* the entrypoints specific ones. The entry
points are invoked in the module's directory, meaning that they can use relative path inside of the
game module. This allows for using a wrapper script if more than one command needs to be invoked
like in ``Checker`` in the example above.

Logging
=======

The game module can use both standard output and standard error output streams to produce logs. The
standard output contents visible to ordinary users. The standard error log contents are not visible
to users and can be used to provide additional information for tournament/system administrators for
diagnostic purposes.


*************************
Deploying the game module
*************************

Deploying of the game module is done simply by copying the game module directory to *modules
directory* on worker machines (the ``/var/opcaic/modules/`` directory from
:ref:`installation-instructions`). The worker component will detect the addition of the new game
module automatically. You should be able to see the newly deployed game module under *available
games* listed for each connected worker inside *System* tab in the web application's administration
section.

If the game module requires additional software, make sure it is also installed on the worker
machine and accessible to the user under which the worker process is running.

The OPCAIC platform does not require every game module to be present on all workers in order to
function properly. It is possible to e.g. deploy the new module only on one worker during testing,
and then deploy it on other workers later. However, it is up to the platform administrators to
ensure that all workers use the same version of the game module.


***************************
Configuring the game module
***************************

Once the game module is deployed, the platform needs to be configured to use it properly. To do so,
enter the administration section, and under ``games`` subsection, select ``Create new game`` and
fill out the game's information. The ``Key`` property should be the name of the game module
directory which was deployed to workers.

Once the game is configured, new tournaments in this game can be created.


*****************
Advanced features
*****************

Tournament specific game configuration
======================================

The platform allows to specify additional configuration options for the game. Imagine a module for
some third person shooter game in deathmatch mode. The relevant options could be e.g. delay before
respawning a player, name of the map where the match should take place, duration of the game and
others. We might want to host different tournaments with different values for these options without
having to create a custom game module for each combination of them.

Adding custom configuration options
-----------------------------------

To allow such advanced tournament configuration, visit the Configuration tab in the edit game
page. There it is possible to specify JSON schema of all the configuration options which should be
available for customization. It also generates a preview of the form which will be displayed as part
of the page when creating a new tournament in the given game. We recommend using tools like
https://jsonschema.net which can generate a JSON schema from example JSON file.

.. tip::
    You can use features of JSON schema to constrain the allowed inputs for the genereated form, as
    well as specifying default values to be filled in the form. Several examples of different json
    schemata used to generate forms can be found at `live playground
    <https://rjsf-team.github.io/react-jsonschema-form/>`_ of the library used to generate the said
    forms.

Using the custom configuration
------------------------------

The custom configuration will be provided by the game module as ``config.json`` file inside the
additional files directory, which is the first argument to all entry points.

Security and sandboxing
=======================

The OPCAIC platform **does not** provide any sandboxing of the code provided by users on its
own. The reason for this is that it would be very hard to find a solution that would fit all
possible scenarios (launching a process per user solution vs. loading the solution as a .dll from a
single process). However, the game module implementation may provide further security by launching
the game and individual submissions in a sandboxed environment.
