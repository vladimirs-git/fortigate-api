fortigate-api
=============

Python package to configure Fortigate (Fortios) devices using REST API and SSH.
With this package, you can change objects in the Fortigate. The most commonly used `Objects`_
are implemented in the `FortigateAPI`_ methods, but you can manipulate any other objects
that can be accessed through the REST API using the `Fortigate`_ methods.
You can also get and change the Fortigate configuration through SSH.

Main features:

- REST API to create, delete, get, update objects. Move policy before, after other policy
- Session-based (user, password) and Token-based authentication
- SSH Netmiko connector to work with CLI commands
- Usage examples in `./examples`_

Requirements: Python >=3.8
This project on `GitHub`_.


----------------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 1
   :caption: Contents:

    NbApi <api/nb_api.rst>
    NbForager <foragers/nb_forager.rst>
    NbBranch <branch/nb_branch.rst>
    NbValue <branch/nb_value.rst>
    Demo <demo.rst>


----------------------------------------------------------------------------------------

Installation
------------

Install the package from pypi.org release

.. code:: bash

    pip install fortigate-api

or install the package from github.com release

.. code:: bash

    pip install https://github.com/vladimirs-git/fortigate-api/archive/refs/tags/1.3.2.tar.gz

or install the package from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/fortigate-api


----------------------------------------------------------------------------------------------------

Quickstart
==========



----------------------------------------------------------------------------------------

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


----------------------------------------------------------------------------------------

.. _`GitHub`: https://github.com/vladimirs-git/fortigate-api
