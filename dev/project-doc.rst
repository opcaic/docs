##############################
 Project development progress
##############################

This section briefly describes the progress of the project development. The implementation started
right after detailed specification defense (June 7th) by setting in place rules for collaboration
between the members of the team, like how often the team will meet and discus further development,
which development tools we will use etc. We decided to use `Azure DevOps
<https://azure.microsoft.com/en-us/services/devops/>`_ for task management, and `Slack
<https://slack.com/intl/en-cz/>`_ for communication. After setting up mentioned tools, we continued
by creating git repositories, setting up *Continuous integration* using `Azure Pipelines
<https://azure.microsoft.com/en-us/services/devops/pipelines/>`_ from Azure DevOps to automatically
check if the submitted code builds and all unit tests pass. We also configured Azure DevOps to emit
events into dedicated slack channels so team members would be alerted on events like failing build.

We also set rules on how the contribution to the codebase should be done. As a rule, no code could
be pushed directly to the main ``dev`` branch. Instead, every code would go to a dedicated git
branch for that particular change and have a *pull request* submitted. The changes would be then
merged if all following conditions are satisfied:

  - the build succeeds and all unit tests pass,
  - one of the other team members reviews the changes and approves the merge, and
  - there are no unresolved comments from code review.

The pull request would be then *squashed* and added in a single commit to the ``dev`` branch. This
approach did not work flawlessly in the early stages of development which was done around the exam
period of the summer semester. It happened often that the infrastructural code developed as part of
one pull request was then immediately needed by the next feature being worked on. And since the team
members needed to focus on studying for the exams, the code review part had to wait days until a
some team member was available. This led to either:

  - postponing the work until the pull request is merged to ``dev`` and the newly developed code is
    available, and working on some other feature.
  - basing the new feature branch not on ``dev``, but on the branch with the required code.

The second approach then led to ugly merge conflicts because of the commit squashing and was not
used often. Also, there were a lot of merge conflicts as the server development was done by 3 team
members at the time.

Later in the develpment we acquired a virtual machine we could use as our testing environment. We
then established a *Release pipeline* which would automatically deploy the complete project onto the
virtual machine every time a pull request is merged.

However, during the summer when most development work was done, infrastructure code was more or less
finalized, the rules we have established helped to keep the development environment stable and
functional for testing. Keeping testing environment functional was also crucial for web application
development, because most of the later development was done against the testing environment server.


******************************
 Server development
******************************

In the beginning of the server development, we used *3-tier* architecture, organizing classes into
*Controller* layer, *Service* layer and *Repository* layer. To us, it seemed a good Idea at the
time, however we later discovered some issues when the code base grew singificantly large:

  - When adding/modifying a feature, code changes needed to be made at all three layers, and was
    made difficult by keeping source code files grouped by the layer.
  - Each method on classes in the Service layer was mostly used only when processing a one
    particular request type.
  - Application logic started leaking into Repository layer. For example transitioning tournaments
    into Finished state required complex filter in the database query, and the exact conditions
    needed to be inside the repository implementation, far away from code processing the data.

After some consideration, we started looking for a better solution, and we discovered MediatR
library and *vertical slices* architecture. This architecture localizes code which handles a single
request, also called *use-case*. This means that all changes to e.g. how new users are created now
need to be done to a few key classes, mostly in the same source code file or folder. This greatly
simplified code navigation in our project and sped up following development.

As part of the search for suitable solution, we encountered other practices which helped us move as
much application logic as possible into the application project. One of the example worth mentioning
was *specification pattern* which allowed us to move the database query specification into
application project, and the repository class would be then only responsible to translating this
query into appropriate query language (in our case PSQL via EntityFramework).

At the time of writing this text, there are still small parts of code which were not refactored, but
all team members were satisfied with the refactor results and consider it a great improvement.

******************************
 Web app development
******************************

In the React ecosystem, it is quite common to base a new project on an already existing boilerplate project, because setting up tools like Webpack, static code anylysis etc. can be quite complext and time-consuming. We decided to use the `react boilerplate <https://github.com/react-boilerplate/react-boilerplate>`_ project because we had some previous experience with it and it looked like it should provide most of the functionality that we needed. 

The next step was to choose a UI component library that would provide at least basic UI components like tables, lists, menus, forms, etc. We decided to use the `Ant Design <https://ant.design/>`_ library because it provides most of the components that we needed and is very popular in the React community. We ended up building almost the whole administration area with these UI components, which saved us a lot of time. The public part of the application is a combination of premade components and our own design.

As we were not very experienced with creating applications in React, it took us some time to setup the whole project and decide how should we approach the whole task. One of the first decisions was to divide the whole project into two different modules - the public module and the admin module - because we would often have logic that needed to be implemented differently for users and admins. We also had to setup things like authorization, localization, etc. The next big step was to implement a functionality that would allow us to easily call the API server and handle CRUD operations. To handle that, we created a basic resource manager which was later often improved as we needed to support more complex use cases. 

At the end of the development process, we were able to easily implement all the frequently needed functionalities like tables with AJAX pagination and sorting/filtering, forms with both client and server error messages, new pages with routing, etc.

******************************
 Dropped features
******************************

As the prototype was slowly transforming to a full product and we started to work on implementing
concrete tournament formats and types. We discovered that some of the features specified in the project's
formal requirements were badly designed and did not make much sense in the resulting program. One
such feature was *Average ranking*. The other two types of ranking - *Maximum* and *Minimum*
determined the winner of a match based on which player had higher/lower score. The avereage ranking
was originally intended for singleplayer games (puzzles) so that the player's submission could be
evaluated multiple times (with different version/instances of the puzzle) and the resulting score
was to be the average of all the scores. We realized it would be difficult to achieve fairness in
such scenarios, e.g. if some submission arrived significantly later than others. We also realized
that producing average scoring over multiple puzzles could be done internally by the underlying game
module without any support needed from the platform. After discussion with the project supervisor,
we decided to drop the Average ranking feature.

The average ranking feature is not the only one that was dropped, due to time constraints, we
decided to drop support for multiplayer game types (meaning games with matches with 2 or more
participants). Thus, conducting e.g. deathmatch tournaments between groups of bots is not supported
in the initial release of the project. However, we still consider it an interesting feature and are
including it in a roadmap for further project development.

************************************
 Testing, bug fixing, documentation
************************************

After the end of summer holidays, after about 4 and half months of development, we had almost fully
working implementation, with only a few minor features still in development. The last month of
development was spent primarily on testing, bug fixes, and user interface improvements.

When it was time to start writing the projects documentation, we were looking for a solution that
would allow us to write the documentation once and be able to produce both printed and online
version. After some investigation, we discovered `sphinx <http://www.sphinx-doc.org/en/master/>`_
which is able to generate documentation multitude of formats, including HTML and LaTeX. We also
discovered `Read The Docs <https://readthedocs.org>`_ which is a free service for hosting online
documentation and directly supports sphinx. Use of sphinx saved us a lot of time which would
otherwise be spent on keeping both web and offline documentation synchronized.
