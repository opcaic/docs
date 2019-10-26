# OPCAIC documentation repository

This repository contains source code for the online documentation of the OPCAIC platform. The web form is hosted on opcaic.readthedocs.io.

To build the documentation locally, you may need to install additional python libraries listed in the `requirements.txt` file

    pip install -r requirements.txt
    
Then you can can use the `make html` command to build the web pages, the result will be put into the `_build` directory. You can achieve live preview via `make livehtml` on `localhost:8000`.
