fortigate-api
=============

Python package to configure Fortigate (Fortios) devices using REST API and SSH.
With this package, you can modify objects in the Fortigate. The most commonly used :ref:`Objects`
are implemented in the :ref:`FortigateAPI` methods, but you can manipulate any other objects
that can be accessed through the REST API using the :ref:`Fortigate` methods.
Additionally, you can retrieve and modify the Fortigate configuration through :ref:`Ssh`.

Main features:

- REST API to create, delete, get, update objects. Move policy before, after other policy
- Session-based (user, password) and Token-based authentication
- SSH Netmiko connector to work with CLI commands
- Usage :ref:`Examples`

Python >=3.8 required.

This project on `GitHub`_.


----------------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 1
   :caption: Contents:

    FortigateAPI <FortigateAPI.rst>
    Fortigate <Fortigate.rst>
    Objects <objects.rst>
    SSH <SSH.rst>
    Examples <examples.rst>


----------------------------------------------------------------------------------------

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

- Create address in the Fortigate,
- Get all addresses from the Fortigate,
- Get filtered address by name (unique identifier),
- Filter address by operator *contains* `=@`,
- Update address data in the Fortigate,
- Delete address from the Fortigate by name (unique identifier),
- Check for absence of address in the Fortigate,

.. code:: python

    import logging
    from pprint import pprint

    from fortigate_api import FortigateAPI

    logging.getLogger().setLevel(logging.DEBUG)

    HOST = "host"
    USERNAME = "username"
    PASSWORD = "password"

    fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)

    # Create address in the Fortigate
    data = {
        "name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.252",
        "type": "ipmask",
    }
    response = fgt.address.create(data)
    print(f"address.create {response}")  # address.create <Response [200]>

    # Get all addresses from the Fortigate
    addresses = fgt.address.get()
    print(f"All addresses count={len(addresses)}")  # All addresses count=14

    # Get filtered address by name (unique identifier)
    addresses = fgt.address.get(uid="ADDRESS")
    pprint(addresses)
    #  [{"comment": "",
    #    "name": "ADDRESS",
    #    "subnet": "127.0.0.100 255.255.255.252",
    #    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
    #    ...
    #    }]

    # Filter address by operator *contains* `=@`
    addresses = fgt.address.get(filter="subnet=@127.0")
    print(f"Filtered by `=@`, count={len(addresses)}")  # Filtered by `=@`, count=2

    # Update address data in the Fortigate
    data = dict(name="ADDRESS", subnet="127.0.0.255 255.255.255.255", color=6)
    response = fgt.address.update(uid="ADDRESS", data=data)
    print(f"address.update {response}")  # address.update <Response [200]>

    # Delete address from the Fortigate by name (unique identifier)
    response = fgt.address.delete(uid="ADDRESS")
    print(f"address.delete {response}")  # address.delete <Response [200]>

    # Check for absence of address in the Fortigate
    response = fgt.address.is_exist(uid="ADDRESS")
    print(f"address.is_exist {response}")  # address.is_exist False

    fgt.logout()



:py:class:`.Fortigate` demonstration.

- Create address in the Fortigate,
- Get address by name (unique identifier) from the Fortigate,
- Update address data in the Fortigate,
- Delete address from the Fortigate by name (unique identifier),

.. code:: python

    import logging
    from pprint import pprint

    from fortigate_api import Fortigate

    logging.getLogger().setLevel(logging.DEBUG)

    HOST = "host"
    USERNAME = "username"
    PASSWORD = "password"

    fgt = Fortigate(host=HOST, username=USERNAME, password=PASSWORD)

    # Creates address in the Fortigate
    data = {
        "name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.252",
        "type": "ipmask",
    }
    response = fgt.post(url="api/v2/cmdb/firewall/address/", data=data)
    print(f"POST {response}", )  # POST <Response [200]>

    # Get address by name (unique identifier) from the Fortigate
    addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
    addresses = [d for d in addresses if d["name"] == "ADDRESS"]
    pprint(addresses)
    #  [{"comment": "",
    #    "name": "ADDRESS",
    #    "subnet": "127.0.0.100 255.255.255.252",
    #    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
    #    ...
    #    }]

    # Updates address data in the Fortigate
    data = dict(color=6)
    response = fgt.put(url="api/v2/cmdb/firewall/address/ADDRESS", data=data)
    print(f"PUT {response}")  # PUT <Response [200]>

    # Delete address from the Fortigate by name (unique identifier)
    response = fgt.delete(url="api/v2/cmdb/firewall/address/ADDRESS")
    print(f"DELETE {response}", )  # DELETE <Response [200]>

    fgt.logout()


----------------------------------------------------------------------------------------

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


----------------------------------------------------------------------------------------

.. _`GitHub`: https://github.com/vladimirs-git/fortigate-api
