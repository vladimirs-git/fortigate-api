fortigate-api
=============

Python package to configure Fortigate (Fortios) devices using REST API and SSH.
With this package, you can modify objects in the Fortigate. The most commonly used :ref:`Objects`
are implemented in the :ref:`FortigateAPI` methods, but you can manipulate any other objects
that can be accessed through the REST API using the :ref:`Fortigate` methods.
Additionally, you can retrieve and modify the Fortigate configuration through :ref:`SSH`.

Main features:

- REST API to create, delete, get, update objects. Move policy before, after other policy
- Session-based (user, password) and Token-based authentication
- SSH Netmiko connector to work with CLI commands
- Usage :ref:`Examples`


This project on `GitHub`_.

Python >=3.8 required.

----------------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 1
   :caption: Contents:

    FortigateAPI <fortigate_api.rst>
    Fortigate <fortigate.rst>
    Objects <objects/objects.rst>
    Address <objects/address.rst>
    SSH <ssh.rst>
    Examples <examples.rst>


----------------------------------------------------------------------------------------------------

Quickstart
==========

Install the package from pypi.org

.. code:: bash

    pip install fortigate-api

or from github.com release

.. code:: bash

    pip install https://github.com/vladimirs-git/fortigate-api/archive/refs/tags/1.3.2.tar.gz

or from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/fortigate-api


:py:class:`.FortigateAPI` demonstration.
TODO

.. code:: python

    from pprint import pprint


:py:class:`.Fortigate` demonstration.
TODO

.. code:: python

    from pprint import pprint


----------------------------------------------------------------------------------------

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


----------------------------------------------------------------------------------------

.. _`GitHub`: https://github.com/vladimirs-git/fortigate-api
