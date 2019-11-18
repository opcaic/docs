.. _warlight-module:

################################
 Warlight game module
################################


**************************
 Overview
**************************

To show the overall functionality of the platform, we implemented an example game module to run the
tournaments.  We chose the game Warlight, written in Java, which is used during lectures of
Artificial Intelligence. This game was already implemented in open-source, freely available at
https://github.com/medovina/Warlight. We edited the project so that it would fit the interface of
our platform, and its desired functionality.  The final game module is open-source, available at
https://github.com/opcaic/Warlight. For more information about the general game modules interface,
see section *Adding a new game to the platform*.


**************************
 Java Modules
**************************

There are several (java) modules in the project, which we will briefly describe in this section. The
game engine is implemented in modules *Conquest-Bots* and *Conquest*.  They handle all the logic
concerning the game itself, such as creating matches in the game, handling bots playing the match
and producing the results.  These modules have origin in the source project.

Module *Conquest-Tournament* is also from the original project, where it was used to run the
tournaments used during the lectures. We edited this project, so that it would fit the needs and
interface of our platform.

Modules *Conquest-Checker*, *Conquest-Compiler*, *Conquest-Validator* correspond to the appropriate
entrypoints used during validation of players' submissions.  Lastly, module *Conquest-Executor* is
used to run the matches and produce their results.

Dependencies
=======================

Apart from several dependencies inside the project, some of the modules are aslo dependent on
libraries *jsap.jar* and *json.jar* (package org.json).  We also edited the game itself, so that
it's needs a configuration file, named *config.json*. This file specifies basic properties of the
game to be run:

seed
    Specifies seed to be used by the internal random number generator during the game evaluation

botCommandTimeoutMillis
    Time limit for bots' turns, in milliseconds.  

startingArmies
    Number of armies to start the game with. 

maxGameRounds
    Maximum number of game rounds to play. If there is no winner after that number of rounds, the
    winner is determined by the game based on the armies and regions the players currently have.

fightMode
    Mode of the game the supported values are:

        - ORIGINAL_A60_D70

            Original Warlight fight without luck:

                - each attacking army has 60% chance to kill one defending army
                - each defending army has 70% chance to kill one attacking army

        - CONTINUAL_1_1_A60_D70

                RISK-like attack

                    - fight happens in round until one of side is fully wiped out
                    - each round there is a 60% chance that 1 defending army is killed and 70%
                      chance that 1 attacking army is killed (independent variables)

games-count
    Determines the number of games to play. This should be an odd number so that there is always a
    clear winner.

Example configuration file follows:

.. code-block:: js

    {
        "seed": 42,
        "botCommandTimeoutMillis": 5000,
        "startingArmies": 5,
        "maxGameRounds": 100,
        "fightMode": "CONTINUAL_1_1_A60_D70",
        "games-count": 1
    }


Building the modules
==========================

All the entrypoint modules should be built to executable jar files. This can be done either in most
of the popular IDEs for Java (such as IntelliJ or Eclipse). Alternatively, they can be built
directly through command line/bash. The appropriate commands are::

    javac <ModuleFolder> -classpath <path to needed libraries> *
    jar cvf <ModuleName>.jar <ModuleFolder>

To make the jars executable, there are *Manifest.mf* files in *META-INF* folders, specifying the
locations of main classes, placed in the folders of the entrypoint modules.  Modules of entrypoints
are not dependent on any libraries, and thus the *classpath* option can be omitted.

Apart from building the entrypoint modules, the *Conquest-Tournament* module has to be built to a
jar, too. For information about that, see the pages of the original project.

Running the entrypoints
==========================

Conquest-Checker
--------------------------

Checker entrypoint can be invoked by calling::

    java -jar Conquest-Checker.jar <path to libraries> <path to source files folder>

First argument, *path to libraries*, is not used by the module, and is present only to suffice the
interface of the platform.

Upon executing, the module checks whether there is exactly one java file in the *source files
folder*, and exits with either code 0 (success) or 200 (error), depending on the result of the
check.

Conquest-Compiler
--------------------------

This entrypoint is dependent on libraries *Conquest.jar* and *Conquest-Bots.jar*, which must be
present in working directory when calling the entrypoint. Compiler entrypoint can be invoked by
calling::

    java -jar Conquest-Compiler.jar <path to libraries> <path to source files folder> <path to store compiled bot>

First argument, *path to libraries*, is not used by the module, and is present only to suffice the
interface of the platform.  Upon executing, the module tries to compile the bot present in java file
in the *source files folder*. The resulting jar file is placed in the *compiled bot folder*.  If
everything works correctly, the compiler exits with code 0, else with code 200.

Conquest-Validator
--------------------------

This entrypoint is dependent on library *Conquest-Tournament.jar*, which must be present in working directory when calling the entrypoint.
Validator entrypoint can be invoked by calling::

    java -jar Conquest-Validator.jar <path to config> <path to the compiled bot>

First argument, *path to config*, specifies the location of the *config.json* file, needed to run
the game. Upon calling, the validator tries to run a game with both players represented by the bot
in the *compiled bot folder*. If the game finishes successfully, the program exits with code 0, else
with code 200.

Conquest-Executor
--------------------------

This entrypoint is dependent on library *Conquest-Tournament.jar*, which must be present in working
directory when calling the entrypoint.  Validator entrypoint can be invoked by calling::

    java -jar Conquest-Validator.jar <path to config> <path to the compiled bot 1> <path to the compiled bot 2> <path to the results>

First argument, *path to config*, specifies the location of the *config.json* file, needed to run
the game. Upon calling, the executor runs the game with the bots in the specified *compiled bot*
folders. If everything works correctly, the program ends with code 0, with code 200 otherwise.  The
results of the game are produced to the *result folder*. The most important of them is
*match-results.json*, which determines the actual results of the match.  Its format is as follows.

.. code-block:: js

    {
        "results":
            [
                {
                    "score":0,
                    "roundsWon":0,
                    "regions":35,
                    "armies":446
                },
                {
                    "score":1,
                    "roundsWon":3,
                    "regions":91,
                    "armies":1769
                }
            ]
    }

The meaning of the individual fileds inside the results array is following:

score
    Contains 1 for winner of the match and 0 for the loser of the match.

roundsWon
    The number of game rounds won by the player.

regions
    Sum of the number of regions held at the and of each round.

armies
    Sum of the number of armies posessed at the and of each round.


Entry-points configuration
--------------------------

To finish the integration of the warlight game to the platform, The commands to invoke the
individual entry points must be specified in an ``entrypoints.json`` file. Since each entry point is
implemented using a wrapper in java, the configuration must specify how to invoke the respective
java *.jar* module:

.. code-block:: js
   :caption: *entrypoints.json* file for the warlight game module.

    {
        "Checker": {
            "Executable": "java",
            "Arguments": [
                "-jar",
                "./checker/Conquest-Checker.jar"
            ]
        },
        "Compiler": {
            "Executable": "java",
            "Arguments": [
                "-jar",
                "./compiler/Conquest-Compiler.jar"
            ]
        },
        "Validator": {
            "Executable": "java",
            "Arguments": [
                "-jar",
                "./validator/Conquest-Validator.jar"
            ]
        },
        "Executor": {
            "Executable": "java",
            "Arguments": [
                "-jar",
                "./executor/Conquest-Executor.jar"
            ]
        },
        "Cleanup": {
            "Executable": "echo",
            "Arguments": [
                "0"
            ]
        }
    }

The warlight module does not utilize the Cleanup entry point, so a no-op command is used instead.

Submissions
===========

Valid submissions for this game module must contain *exactly one* .java file with the agent's
implementation. The submitted file must create a ``conquest.bot.custom`` package, and the
implementation must extend the ``GameBot`` interface. The source code for the random bot located at
*Conquest-Bots/src/conquest/bot/custom/RandomBot.java* in the module's repository can be used as a
starting point

More information about writing the bot can be found in the `original warlight repository <https://github.com/medovina/Warlight>`_
