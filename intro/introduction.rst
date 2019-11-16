##############
 Introduction
##############

OPCAIC is an abbreviation of **O**\ nline **P**\ latform for **C**\ onducting **AI** **C**\
ompetitions. It is a complex solution for hosting and fully automatic execution of tournaments
between artificial agents in a multitude of games. The platform features a modern web interface and
distributed computing capability suitable for conducting multiple tournaments simultaneously. It's
primary goal is to serve as an automated tool for conducting tournaments held during various
lectures at our university (such as Artificial Intelligence or Multi-Agent systems), however, on a
broader scale, it can be employed in the context of AI competitions held at various academic
conferences (such as CIG, AIIDE or IJCAI).

*************
Main Features
*************

The main features are:

    - Single-player games (puzzles) and two-player games support
    - Multiple supported tournament formats
      
        - single/double elimination brackets
        - table (round robin)
        - ELO

    - Multiple visibility settings per tournament:

        - public and private (invitation-only) tournaments
        - hiding user names (anonymizng) of authors of competing bots
        - showing all matches vs only matches in which user's bot participates

    - Accepting solutions in source code or compiled form.
    - Granular game configuration for each tournament
    - Ability to add new custom games

***********
Terminology
***********

At first, we present an overview about the terminology being used in the documentation, covering the
most important features of the platform.

    - *Game* - a game/puzzle to organize the tournaments in 
    - *Match* - a match/round of a game, played by users' bots
    - *Bot* - any bot/solution participating in the matches
    - *Submission* - a source code of the bot, submitted by the competitor
    - *Tournament* - a contest of bots, in a specific game, with specific properties 
    - *Guest* - anyone visiting our website, who is not logged in
    - *Competitor/User* - a logged in user, someone who contests in the tournaments 
    - *Organizer* - user with permission to create and manage tournaments
    - *Admin* - administrator of the web, manages the platform
    - *Game module* - a “blackbox” which runs the game itself and produces appropriate results

****************
Example use-case
****************

To provide a better overview on the usage of the platform, we present an example-use case in this
section. It covers the main pipeline of creating and evaluating tournament, and it's divided to
three parts corresposding to main stages of this pipeline.

Creating a tournament
=====================

At the beginning of the pipeline, there is an organizer with intention to conduct a tournament. He
has to fill some basic information about it, such as name, visibility (public or private - only for
invited users) and so on. Then, the web app provides him a list of currently implemented games and
tournament types (formats, scopes etc.), which he chooses from. After filling all this, the
tournament can be published, making it available for competitors.  Organizer can also invite other
users to his tournament by specifying their emails.

Submitting a solution
=====================

To join a tournament, users of the platform has to create an account first, and log in. After that,
they can browse through available tournaments (public or private they are invited to), and
eventually submit solutions. These solutions has to follow rules specific for different
games/tournaments, such as number of files, language of the source code and so on. The specific
rules for each tournament are listed on tournament's page. Upon submitting, the bot is validated by
the server checking whether it follows game's rules and API. If the validation is successful, the
user has joined the tournament with his bot.

Evaluating a tournament
=======================

This stage of the pipeline happes completely automatically. Depending on the tournament's format and
scope, the server plans matches for the tournament and picks the bots for them from the available
pool of submitted solutions. Then, the server runs the matches and evaluates their results, which
also become available to the users through the website. Until the tournament is finished, this cycle
happens again. Tournament's leaderboards are then published on the website.


*************
Extensibility
*************

The platform can be extended by adding custom games. There are no constraints on the game's
implementation language. All that is required is providing a set of commands which e.g. check for
submission validity or start the game. For more informatino, see :ref:`adding-new-games`.

*******
Roadmap
*******

There are some features and posible improvements for future development

    - N-player games - ability to host e.g. deathmatch tournaments between groups of bots.
    - login using social network accounts - Google, Facebook, etc.
    - Ability to interpret additional match data in web application: e.g. replays of matches.
    - live feedback on the submission validaiton process when given window is opened in web
      application
