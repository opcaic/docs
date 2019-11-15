################################
 User documentation
################################

**************************
 General basics
**************************

Homepage
==========================

The *Homepage* contains a list of featured tournaments and games and provides links to corresponding list pages.

User dashboard
==========================

The *User dashboard* page replaces the *Homepage* for logged in users. It contains the most important about recent matches and submissions:

- *My recent matches* - Displays all the recent matches of the current user across all the tournaments
- *My recent submissions* - Displays all the recent submissions of the current user across all the tournaments
- *My running tournaments* - Displays all the running tournaments where the current user participated

Registration
==========================

Users can register by clicking the *Register* link in the top menu of the website. By registering, users then allowed to submit their own solutions to tournaments on our platform.

The registration form contains multiple fields:

- *Username* - will be seen by other players when participating in tournaments
- *Email* - will be used to log into the website
- *Password* - must be at least 8 chars long
- *Captcha* - to prevent spam bots
- *Privacy policy*

After clicking the *register* button, the user is redirected to the *Registration successful* page that informs them that we have sent them a confirmation email with a link to active the account. Until the account is activated, the user is not able to log in.

The last step is to click the link in the confirmation email that redirects users back to our website and activates their account. It may happen that the link has already expired and in that case we provide a link to the *Resend confirmation email* page that lets users request another confirmation email to be sent.

Login
==========================

Users can log in by clicking the *Login* link in the top menu of the website. 

Logout
==========================

Users can loggout by clicking the user icon in the top menu a then choosing *Logout*.

Forgotten password
==========================

If a user does not know his or or her password, it is possible to change it through the *Forgetten password* page. This page is accessible through a link below the login form.

To change the password, a user has to provide the registration email address and the wait for a *reset password* email. The email contains a link that leads to the *Reset password* page where users can choose their new passwords.

Settings
==========================

The *Settings* page can be accessed when logged in by clicking the user icon in the top menu a then going to *Settings*.

Profile
--------------------------

The *Profile* page lets users see and change their profile information.

- *Organization* - if a user is affiliated with any organization like school or company, this field can be filled in and the organization will be then publicly displayed on the leaderboard page.

Change password
--------------------------

The *Change password* page lets users change their password if they know the current one.

Language
==========================

The website language can be changed by clicking the *Language* button located in the top menu and then choosing a language from the list.


**************************
 Tournaments
**************************

Tournaments on our website are configured by setting tournament's properties, such as *tournament format*, *scope* and *ranking strategy*.
These properties define the process of evaluating given tournament, and also the way how to measure its results.

Tournament properties
==========================

Scope
--------------------------
Tournament *scope* defines the time the tournament is opened for submissions, and when will the tournament be evaluated. 

First of the scopes is **deadline**, which means that there is a certain date, until when the tournament is opened for competitors. 
After that date, all the matches of the tournament are planned and executed. The other type is an **ongoing** tournament. 
Such tournament is opened for submissions all the time, and its matches are planned and executed continuously.

Format
--------------------------
Tournament *format* defines the way how to plan matches and also how to determine tournament's leaderboards.

The first format is **single player**, where there is only one way how to plan matches. In that format, players are ranked
directly based on the points they obtain in the matches.

For games of two players, there are four formats available. First one is **Elo**, the most usual system of ongoing tournaments (https://en.wikipedia.org/wiki/Elo_rating_system). 
Players in ELO are rated based on their relative skill, which is expressed by their "Elo points". These points determine both the leaderboard of the tournament and also serve for 
planning matches, so that they can be planned continuously. The second two formats are **single** and **double elimination** (https://en.wikipedia.org/wiki/Tournament#Knockout) tournaments. 
In such tournaments, the matches are all planned at once, forming an elimination bracket, where the losers are gradually knocked out of the tournament, until there is only the winner left. 
The terms single/double elimination refer to the number of matches a player has to lose to be ultimately eliminated from the tournament. The last format available is a **table** tournament.
In such a tournament, each player plays a match against every other player. Players are then ordered directly by the sum of their score in individual matches.

Ranking strategy
--------------------------
The final tournament property is *ranking strategy*, which determines how will be the players ranked based on the points they obtained in the tournament.

The two implemented ranking strategies are **maximum** and **minimum**, and their meaning is self-explanatory.

Tournament list
==========================

On the tournament list page, users can browse tournaments that were published on the platform.

The page contains a filter with various options:

- *State* - *running* (accepts submission) or *finished* (finished or evaluating submissions)
- *Game* - filter by tournament game
- *Format* - filter by tournament format
- *Scope* - filter by tournament scope
- *Sort by* - either by deadline date (for runnig tournaments) or by finished date (for finished tournaments)

The list contains only tournaments that are visible to the currently logged in user which means that users cannot see tournaments that were created but not yet published. Organizers may also choose to make tournaments only available to invited users, in which case such a tournament does not appear in the list if the user is not invited.

By clicking on the tournament, a user is redirected to the tournament detail page. 

Tournament detail
==========================

The tournament detail page contains all the information related to a single tournament. The page is divided into multiple tabs that can be accessed through the inner page menu. Some tabs are only available to logged in users (*My submissions* and *My matches*). If the tournament accepts submissions, the menu also contains a button that lets users submit a solution to the tournament.

Overview
--------------------------

The *Overview* tab provides basic information about the tournament like its state, scope, format, number of players, etc. It also contains a description of the tournament provided by its organizer. Organizers can also decide to divide the description into multiple pages, in which case a navigation appears on the left-hand side of the tab.

Leaderboard
--------------------------

The *Leaderboard* tab displays the overall standings of the players in the tournament. For ongoing tournaments, leaderboards are provided right after the first match is played. Whereas for tournaments with deadline, leaderboards are displayed only after all the matches are played. 

Some tournaments also provide visualization of the whole tournament - brackets for single and double elimination tournaments, table visualizaton for table tournaments. 

Matches
--------------------------

The *Matches* tab displays all the matches that were played in the tournament and provides access to match details with additional information about the matches. 

Tournament organizers can decide to make the match log private which means that no matches are displayed on this tab and players can only see their own matches on the *My matches* tab.

My matches
--------------------------

The *My matches* tab is only visible to logged in users and displays all the matches where the user participated in.

Match detail
--------------------------

The *Match detail* page can be accessed either from the *Matches* tab or from the *My matches* by clicking the *Detail* button on correspoing row in the list. It contains detailed information about the match - date of execution, participating players and their scores. Some games also provide additional information about each participant or about the match itself.

Submit solution
--------------------------

The *Submit solution* button opens a modal windows that lets users submit their solutions. If the user is not logged in, the windows contains a login link and the users is redirected back after they log in.

There are currently two ways of submitting solutions:

- **multiple files** - Users can upload multiple files by either dragging them to the upload area or clicking the area and choosing the files in the dialog window. This approach is good if the solution consist of only a few files and there are no folders in the solution.
- **single zip file** - For more complex solutions, users can upload a single zip file with the whole solution. The main advantage of such an approach is that these submissions can also contain folders.

After submitting a solution, the user is redirected to the detail of that submission.

My submissions
--------------------------

The *My submissions* tab is only visible to logged in users and displays all their submissions.

Submission detail
--------------------------

The *Submission detail* page can be accessed either from the *My submissions* tab by clicking the *Detail* button on correspoing row in the list. It contains detailed information about the submissions - date of submissions, its validation state and whether the submission is currently active.

The most important information is the **validation state** of a submission. Each submission must pass several validation steps to be considered valid. Only after that can the solution be used in the tournament.

- *Checker* - checks if all required files are present in the submission
- *Compiler* - tries to compile the submission
- *Validator* - smoke tests the compiled submission

**Active** submission is such a submission that is used when executing matches for the tournament. It is currently not possible for a user to choose which submission is active in the tournament. The rule is that the last valid submission is made active.

**************************
 Games
**************************

Game list
==========================

On the *Game list* page, users can browse games that are implemented on the platform. By clicking on a game, the user is redirected to the game detail page. 

Game detail
==========================

The *Game detail* page contains a short description of the game (if it is provided by the administrators) and also a list of all running tournaments in that game.
