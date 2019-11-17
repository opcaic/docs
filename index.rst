.. doc documentation master file, created by
   sphinx-quickstart on Sat Oct 26 20:55:34 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:Authors: - Radek Zikmund
          - Ondřej Nepožitek
          - Michal Lehončák
          - Šimon Stachura
   
Welcome to OPCAIC documentation!
================================

.. only:: html

    .. include:: intro/introduction.rst

.. raw:: latex

   \part{Getting Started}

.. toctree::
   :maxdepth: 2
   :caption: Getting Started:

   intro/introduction.rst
   intro/installation-instructions
   intro/server-configuration
   intro/worker-configuration
   intro/webapp-configuration
   intro/adding-new-game-modules

.. raw:: latex

   \part{User Documentation}
   
.. toctree::
   :maxdepth: 2
   :caption: User Documentation:

   user/user
   user/admin-organizer

.. raw:: latex

   \part{Developer Documentation}
   
.. toctree::
   :maxdepth: 2
   :caption: Developer Documentation:

   dev/dev-environment
   dev/architecture
   dev/server-arch
   dev/security
   dev/worker-backend
   dev/frontend-arch
   modules/warlight
   dev/project-doc

.. only:: latex

   .. include:: dev/conclusion.rst

.. raw:: latex

    \chapwithtoc{List of attachments}
    \section*{USB key with files}

.. only:: latex

    - *bin* - directory with compiled programs, these can be used to install the platform by following the :ref:`installation-instructions`.

        - *server* - compiled server component
        - *worker* - compiled worker component
        - *webapp* - compiled webapp component
        - *modules* - compiled game modules

            - *warlight* - adapted Warlight game for the platform

    - *src* - directory with all platform source code files

        - *server* - shared sources for both server and worker components
        - *webapp* - source code for the web application
        - *warlight* - adapted source code for the warlight game module

    - *html-docs* - Directory with html form of the documentation, read by opening the *index.html*
      file in browser.
    - *config* - directory with example configuration files referenced in the installation instructions.

        - *opcaic.server.service* - systemd unit file for hosting server component as a service
        - *opcaic.worker.service* - systemd unit file for hosting worker component as a service
        - *nginx.conf* - snippets of nginx configuration needed for hosting server and web application component

    - *docs.pdf* - copy of this document
    - *readme.txt* - description of the USB key contents.

.. raw:: latex

    %% addtional lists
    \if@openright\cleardoublepage\else\clearpage\fi
    \addcontentsline{toc}{chapter}{List of Figures}%
    \listoffigures
    %
    \if@openright\cleardoublepage\else\clearpage\fi
    \addcontentsline{toc}{chapter}{List of Code Blocks}%
    \listof{literalblock}{List of Code Blocks}%
    %
    \if@openright\cleardoublepage\else\clearpage\fi
    \pagenumbering{arabic}%
