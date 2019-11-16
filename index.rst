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

   \part{Developer Documentation}
   
.. toctree::
   :maxdepth: 2
   :caption: Developer Documentation:

   dev/dev-environment
   dev/architecture
   dev/server-arch
   dev/frontend-arch
   dev/project-doc

.. raw:: latex

   \part{User Documentation}
   
.. toctree::
   :maxdepth: 2
   :caption: User Documentation:

   user/user
   user/admin-organizer

.. todolist::
