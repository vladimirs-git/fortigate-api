
.. image:: https://img.shields.io/pypi/v/fortigate-api.svg
   :target: https://pypi.python.org/pypi/fortigate-api
.. image:: https://img.shields.io/pypi/pyversions/fortigate-api.svg
   :target: https://pypi.python.org/pypi/fortigate-api
.. image:: https://img.shields.io/github/last-commit/vladimirs-git/fortigate-api
   :target: https://pypi.python.org/pypi/fortigate-api


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

----------------------------------------------------------------------------------------------------


Requirements
------------

Python >=3.8

----------------------------------------------------------------------------------------------------


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


.. contents:: **Contents**

----------------------------------------------------------------------------------------------------


Objects
-------
The objects implemented in `FortigateAPI`_.
To get an idea of the objects, you can change the *hostname* in the following URLs and
look it in the Fortigate web management interface. The first URL is for the Web GUI, the second
one is for the REST API. Not all object implemented in `FortigateAPI`_ (only the most used by me),
access to any other objects is available via `Fortigate`_.

===================== ==============================================================================
Object                GUI and REST API URL to the object (FortiOS v6.4)
===================== ==============================================================================
`Address`_            https://hostname/ng/firewall/address

                      https://hostname/api/v2/cmdb/firewall/address/

`AddressGroup`_       https://hostname/ng/firewall/address

                      https://hostname/api/v2/cmdb/firewall/addrgrp/

`Antivirus`_          https://hostname/ng/utm/antivirus/profile

                      https://hostname/api/v2/cmdb/antivirus/profile/

`Application`_        https://hostname/ng/utm/appctrl/sensor

                      https://hostname/api/v2/cmdb/application/list/

`DhcpServer`_         https://hostname/ng/interface/edit/{name}

                      https://hostname/api/v2/cmdb/system.dhcp/server/

`ExternalResource`_   https://hostname/ng/external-connector

                      https://hostname/api/v2/cmdb/system/external-resource/

`Interface`_          https://hostname/ng/interface

                      https://hostname/api/v2/cmdb/system/interface/

`InternetService`_    https://hostname/ng/firewall/internet_service

                      https://hostname/api/v2/cmdb/firewall/internet-service/

`IpPool`_             https://hostname/ng/firewall/ip-pool

                      https://hostname/api/v2/cmdb/firewall/ippool/

`Policy`_             https://hostname/ng/firewall/policy/policy/standard

                      https://hostname/api/v2/cmdb/firewall/policy/

`Schedule`_           https://hostname/ng/firewall/schedule

                      https://hostname/api/v2/cmdb/firewall.schedule/onetime/

`Service`_            https://hostname/ng/firewall/service

                      https://hostname/api/v2/cmdb/firewall.service/custom/

`ServiceCategory`_    https://hostname/ng/firewall/service

                      https://hostname/api/v2/cmdb/firewall.service/category/

`ServiceGroup`_       https://hostname/ng/firewall/service

                      https://hostname/api/v2/cmdb/firewall.service/group/

`SnmpCommunity`_      https://hostname/ng/system/snmp

                      https://hostname/api/v2/cmdb/system.snmp/community/

`VirtualIp`_          https://hostname/ng/firewall/virtual-ip

                      https://hostname/api/v2/cmdb/firewall/vip/

`Zone`_               https://hostname/ng/interface

                      https://hostname/api/v2/cmdb/system/zone/
===================== ==============================================================================


----------------------------------------------------------------------------------------------------

FortigateAPI
------------
**FortigateAPI(host, username, password, scheme, port, timeout, vdom)**
Set of methods for working with the most commonly used `Objects`_.

=============== ======= ============================================================================
Parameter        Type    Description
=============== ======= ============================================================================
host            *str*   Firewall ip address or hostname
username        *str*   Administrator name. Mutually exclusive with token
password        *str*   Administrator password. Mutually exclusive with token
token           *str*   Administrator token. Mutually exclusive with username and password
scheme          *str*   (optional) "https" (default) or "http"
port            *int*   (optional) TCP port, by default 443 for "https", 80 for "http"
timeout         *int*   (optional) Session timeout minutes (default 15)
verify          *str*   (optional) Enable SSL certificate verification for HTTPS requests. True -  enable, False - disable (default)
vdom            *str*   Name of virtual domain (default "root")
=============== ======= ============================================================================


----------------------------------------------------------------------------------------------------

Address
-------
Python examples `./examples/address.py`_

Python examples `./examples/address_token.py`_

FortiOS v6.4 data example `./examples/yml/address.yml`_

.. code:: python

    from fortigate_api import FortigateAPI

    fgt = FortigateAPI(host="host", username="username", password="password")

    # Create address
    data = {"name": "ADDRESS",
            "obj-type": "ip",
            "subnet": "127.0.0.100 255.255.255.252",
            "type": "ipmask"}
    response = fgt.address.create(data)

    # Get all addresses
    addresses_all = fgt.address.get()

    # Get address by name
    addresses_by_name = fgt.address.get(uid="ADDRESS")

    # Get address by operator contains \"=@\"
    addresses_contains = fgt.address.get(filter="subnet=@127.0")


create()
........
**FortigateAPI.address.create(data)**
Create address-object in the Fortigate.

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the address-object
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created in the Fortigate


delete()
........
**FortigateAPI.address.delete(uid, filter)**
Delete address-object from the Fortigate.
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Unique identifier. Name of the address-object. Used to delete a single object
filter          *str*, *List[str]*  Filters address-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than return *<Response [200]>*
=============== =================== ================================================================

Return
    Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


get()
.....
**FortigateAPI.address.get(uid, filter)**
Gets address-objects, all or filtered by some of params.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Filters address-object by name (unique identifier). Used to get a single object
filter          *str*, *List[str]*  Filters address-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to get multiple objects
=============== =================== ================================================================

Return
    *List[dict]* List of address-objects


is_exist()
..........
**FortigateAPI.address.is_exist(uid)**
Checks does an address-object exists in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
uid             *str*   Name of the address-object (unique identifier)
=============== ======= ============================================================================

Return
    *bool* True - object exist, False - object does not exist


update()
........
**FortigateAPI.address.update(data, uid)**
Updates address-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the address-object
uid             *str*   Name of the address-object, taken from the `uid` parameter or from data["name"]
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


----------------------------------------------------------------------------------------------------

AddressGroup
------------
Python examples `./examples/address_group.py`_

FortiOS v6.4 data example `./examples/yml/address_group.yml`_

.. code:: python

    from fortigate_api import FortigateAPI

    fgt = FortigateAPI(host="host", username="username", password="password")

    # Create address and address-group in the Fortigate
    data = {"name": "ADDRESS",
            "obj-type": "ip",
            "subnet": "127.0.0.100 255.255.255.255",
            "type": "ipmask"}
    fgt.address.create(data)
    data = {"name": "ADDR_GROUP", "member": [{"name": "ADDRESS"}]}
    fgt.address_group.create(data)

    # Get all address-groups from the Fortigate
    address_groups_all = fgt.address_group.get()

    # Get filtered address_group by name (unique identifier)
    address_groups_name = fgt.address_group.get(uid="ADDR_GROUP")


create()
........
**FortigateAPI.address_group.create(data)**
Create address-group-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the address-group-object
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created in the Fortigate


delete()
........
**FortigateAPI.address_group.delete(uid, filter)**
Delete address-group-object from the Fortigate
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Name of the address-group-object (unique identifier). Used to delete a single object
filter          *str*, *List[str]*  Filters address-group-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than return *<Response [200]>*
=============== =================== ================================================================

Return
    Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


get()
.....
**FortigateAPI.address_group.get(uid, filter)**
Gets address-group-objects, all or filtered by some of params.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Filters address-group-object by name (unique identifier). Used to get a single object
filter          *str*, *List[str]*  Filters address-group-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to get multiple objects
=============== =================== ================================================================

Return
    *List[dict]* List of address-group-objects


is_exist()
..........
**FortigateAPI.address_group.is_exist(uid)**
Checks does an address-group-object exists in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
uid             *str*   Name of the address-group-object (unique identifier)
=============== ======= ============================================================================

Return
    *bool* True - object exist, False - object does not exist


update()
........
**FortigateAPI.address_group.update(data, uid)**
Updates address-group-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the address-group-object
uid             *str*   Name of the address-group-object, taken from the `uid` parameter or from data["name"]
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


----------------------------------------------------------------------------------------------------

Antivirus
---------
**Antivirus** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/antivirus.yml`_

**FortigateAPI.antivirus.create(data)**

**FortigateAPI.antivirus.delete(uid, filter)**

**FortigateAPI.antivirus.get(uid, filter)**

**FortigateAPI.antivirus.is_exist(uid)**

**FortigateAPI.antivirus.update(data, uid)**


----------------------------------------------------------------------------------------------------

Application
-----------
**Application** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/application.yml`_

**FortigateAPI.application.create(data)**

**FortigateAPI.application.delete(uid, filter)**

**FortigateAPI.application.get(uid, filter)**

**FortigateAPI.application.is_exist(uid)**

**FortigateAPI.antivirus.update(data, uid)**


----------------------------------------------------------------------------------------------------

DhcpServer
----------
**DhcpServer** object has the same parameters and methods as `Address`_

Python examples `./examples/dhcp_server.py`_

FortiOS v6.4 data example `./examples/yml/dhcp_server.yml`_

.. code:: python

    from fortigate_api import FortigateAPI

    fgt = FortigateAPI(host="host", username="username", password="password")

    # Create dhcp server
    data = {
        "default-gateway": "192.168.255.1",
        "netmask": "255.255.255.0",
        "interface": "vlan.123",
        "ip-range": [{"start-ip": "192.168.255.2", "end-ip": "192.168.255.254", }],
    }
    fgt.dhcp_server.create(data)

    # Get all dhcp servers
    dhcp_servers = fgt.dhcp_server.get()


**FortigateAPI.dhcp_server.create(data)** Note, in Fortigate is possible to create multiple DHCP servers with the same settings, you need control duplicates

**FortigateAPI.dhcp_server.delete(uid, filter)**

**FortigateAPI.dhcp_server.get(uid, filter)**

**FortigateAPI.dhcp_server.is_exist(uid)**

**FortigateAPI.dhcp_server.update(data, uid)**


----------------------------------------------------------------------------------------------------

ExternalResource
----------------
**ExternalResource** object has the same parameters and methods as `Address`_

Python examples `./examples/external_resource.py`_

FortiOS v6.4 data example `./examples/yml/external_resource.yml`_

**FortigateAPI.external_resource.create(data)**

**FortigateAPI.external_resource.delete(uid, filter)**

**FortigateAPI.external_resource.get(uid, filter)**

**FortigateAPI.external_resource.is_exist(uid)**

**FortigateAPI.external_resource.update(data, uid)**



----------------------------------------------------------------------------------------------------

Interface
---------
**Interface** object has the same parameters and methods as `Address`_

Python examples `./examples/interface.py`_

FortiOS v6.4 data example `./examples/yml/interface.yml`_

.. code:: python

    from fortigate_api import FortigateAPI

    fgt = FortigateAPI(host="host", username="username", password="password")


    # Get all interfaces in vdom \"root\" from the Fortigate
    interfaces = fgt.interface.get()
    print(f"interfaces count={len(interfaces)}")  # interfaces count=21

    # Gets filtered interface by name (unique identifier)
    interfaces = fgt.interface.get(uid="dmz")


**FortigateAPI.interface.create(data)**

**FortigateAPI.interface.delete(uid, filter)**


get()
.....
**FortigateAPI.interface.get(uid, filter, all)**
Gets interface-objects in specified vdom, all or filtered by some of params.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Filters address-object by name (unique identifier). Used to get a single object
filter          *str*, *List[str]*  Filters address-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to get multiple objects
all             *bool*              Gets all interface-objects from all vdom
=============== =================== ================================================================

Return
    *List[dict]* List of interface-objects

**FortigateAPI.interface.is_exist(uid)**

**FortigateAPI.interface.update(data, uid)**


----------------------------------------------------------------------------------------------------

InternetService
---------------
**InternetService** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/internet_service.yml`_

**FortigateAPI.internet_service.create(data)**

**FortigateAPI.internet_service.delete(uid, filter)**

**FortigateAPI.internet_service.get(uid, filter)**

**FortigateAPI.internet_service.is_exist(uid)**

**FortigateAPI.internet_service.update(data, uid)**


----------------------------------------------------------------------------------------------------

IpPool
------
**IpPool** object has the same parameters and methods as `Address`_

Python examples `./examples/ip_pool.py`_

FortiOS v6.4 data example `./examples/yml/ip_pool.yml`_

**FortigateAPI.ip_pool.create(data)**

**FortigateAPI.ip_pool.delete(uid, filter)**

**FortigateAPI.ip_pool.get(uid, filter)**

**FortigateAPI.ip_pool.is_exist(uid)**

**FortigateAPI.ip_pool.update(data, uid)**


----------------------------------------------------------------------------------------------------

Policy
------
Python examples `./examples/policy.py`_

Python examples `./examples/policy_extended_filter.py`_

FortiOS v6.4 data example `./examples/yml/policy.yml`_

.. code:: python

    from fortigate_api import FortigateAPI

    fgt = FortigateAPI(host="host", username="username", password="password")

    # Create policy in the Fortigate
    data = dict(
        name="POLICY",
        status="enable",
        action="accept",
        srcintf=[{"name": "any"}],
        dstintf=[{"name": "any"}],
        srcaddr=[{"name": "all"}],
        dstaddr=[{"name": "all"}],
        service=[{"name": "ALL"}],
        schedule="always",
    )
    fgt.policy.create(data)

    # Get all policies from the Fortigate
    policies_all = fgt.policy.get()

    # Filters policies by name, by operator equals
    policies_name = fgt.policy.get(filter="name==POLICY")


create()
........
**FortigateAPI.policy.create(data)**
Create policy-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the policy-object
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created in the Fortigate


delete()
........
Delete policy-object from the Fortigate
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*, *int*        Identifier of the policy-object. Used to delete a single object
filter          *str*, *List[str]*  Filters policy-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than return *<Response [200]>*
=============== =================== ================================================================

Return
    Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


get()
.....
**FortigateAPI.policy.get(uid, filter)**
Gets policy-objects, all or filtered by some of params.
Only one of the parameters *uid* or *filter* can be used in the same time.
The parameter *efilter* can be combined with "srcaddr", "srcaddr", *filter*

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*, *int*        Filters policy-object by policyid (unique identifier). Used to get a single object
filter          *str*, *List[str]*  Filters policy-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to get multiple objects
efilter         *str*, *List[str]*  Extended filter: "srcaddr", "dstaddr" by condition: equals "==", not equals "!=",  supernets ">=", subnets "<=". Using this option, you can search for rules by subnets and supernets that are configured in Addresses and AddressGroups. See the examples for details.
=============== =================== ================================================================

Return
    *List[dict]* List of policy-objects


is_exist()
..........
**FortigateAPI.policy.is_exist(uid)** Checks does an policy-object exists in the Fortigate

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*, *int*        Identifier of the policy-object
=============== =================== ================================================================

Return
    *bool* True - object exist, False - object does not exist


move()
......
**FortigateAPI.policy.move(uid, position, neighbor)** Move policy to before/after other neighbor-policy

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*, *int*        Identifier of policy being moved
position        *str*               "before" or "after" neighbor
neighbor        *str*, *int*        Policy will be moved near to this neighbor-policy
=============== =================== ================================================================

Return
    Session response. *<Response [200]>* Policy successfully moved, *<Response [500]>* Policy has not been moved


update()
........
**FortigateAPI.policy.update(data, uid)** Updates policy-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the policy-object
uid             *int*   Policyid of the policy-object, taken from the `uid` parameter or from data["policyid"]
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


----------------------------------------------------------------------------------------------------

Schedule
--------
**Schedule** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/schedule.yml`_

**FortigateAPI.schedule.create(data)**

**FortigateAPI.schedule.delete(uid, filter)**

**FortigateAPI.schedule.get(uid, filter)**

**FortigateAPI.schedule.is_exist(uid)**

**FortigateAPI.schedule.update(data, uid)**


----------------------------------------------------------------------------------------------------

Service
-------
**Service** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service.yml`_

**FortigateAPI.service.create(data)**

**FortigateAPI.service.delete(uid, filter)**

**FortigateAPI.service.get(uid, filter)**

**FortigateAPI.service.is_exist(uid)**

**FortigateAPI.service.update(data, uid)**


----------------------------------------------------------------------------------------------------

ServiceCategory
---------------
**ServiceCategory** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service_category.yml`_

**FortigateAPI.service_category.create(data)**

**FortigateAPI.service_category.delete(uid, filter)**

**FortigateAPI.service_category.get(uid, filter)**

**FortigateAPI.service_category.is_exist(uid)**

**FortigateAPI.service_category.update(data, uid)**


----------------------------------------------------------------------------------------------------

ServiceGroup
------------
**ServiceGroup** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service_group.yml`_

**FortigateAPI.service_group.create(data)**

**FortigateAPI.service_group.delete(uid, filter)**

**FortigateAPI.service_group.get(uid, filter)**

**FortigateAPI.service_group.is_exist(uid)**

**FortigateAPI.service_group.update(data, uid)**


----------------------------------------------------------------------------------------------------

SnmpCommunity
-------------
**SnmpCommunity**

Python examples `./examples/snmp_community.py`_

FortiOS v6.4 data example `./examples/yml/snmp_community.yml`_

**FortigateAPI.snmp_community.create(data)**

**FortigateAPI.snmp_community.delete(uid, filter)**

**FortigateAPI.snmp_community.get(uid, filter)**

**FortigateAPI.snmp_community.is_exist(uid)**

**FortigateAPI.snmp_community.update(data, uid)**
Updates snmp-community-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the snmp-community-object
uid             *str*   Name of the snmp-community-object, taken from the `uid` parameter or from data["id"]
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


----------------------------------------------------------------------------------------------------

VirtualIP
---------
**VirtualIP** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/virtual_ip.yml`_

**FortigateAPI.virtual_ip.create(data)**

**FortigateAPI.virtual_ip.delete(uid, filter)**

**FortigateAPI.virtual_ip.get(uid, filter)**

**FortigateAPI.virtual_ip.is_exist(uid)**

**FortigateAPI.virtual_ip.update(data, uid)**


----------------------------------------------------------------------------------------------------

Zone
----
**Zone** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/zone.yml`_

**FortigateAPI.zone.create(data)**

**FortigateAPI.zone.delete(uid, filter)**

**FortigateAPI.zone.get(uid, filter)**

**FortigateAPI.zone.is_exist(uid)**

**FortigateAPI.zone.update(data, uid)**


----------------------------------------------------------------------------------------------------

Fortigate
---------
**Fortigate(host, username, password, scheme, port, timeout, vdom)**
REST API connector to the Fortigate. Contains generic methods (get, put, delete, etc.)
to work with any objects available through the REST API. `Fortigate`_ is useful for working with
objects that are not implemented in `FortigateAPI`_

Python examples `./examples/fortigate.py`_

Python examples `./examples/fortigate_token.py`_

Python examples `./examples/monitor.py`_

.. code:: python

    from fortigate_api import Fortigate

    fgt = Fortigate(host="host", username="username", password="password")

    # Create address in the Fortigate
    data = {"name": "ADDRESS",
            "obj-type": "ip",
            "subnet": "127.0.0.100 255.255.255.252",
            "type": "ipmask"}
    fgt.post(url="api/v2/cmdb/firewall/address/", data=data)

    # Get address data from the Fortigate
    addresses_all = fgt.get(url="api/v2/cmdb/firewall/address/")


=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
host            *str*   Firewall ip address or hostname
username        *str*   Administrator name. Mutually exclusive with token
password        *str*   Administrator password. Mutually exclusive with token
token           *str*   Administrator token. Mutually exclusive with username and password
scheme          *str*   (optional) "https" (default) or "http"
port            *int*   (optional) TCP port, by default 443 for "https", 80 for "http"
timeout         *int*   (optional) Session timeout minutes (default 15)
verify          *str*   (optional) Enable SSL certificate verification for HTTPS requests. True -  enable, False - disable (default)
vdom            *str*   Name of virtual domain (default "root")
=============== ======= ============================================================================


login()
.......
**Fortigate.login()** Login to the Fortigate using REST API


logout()
........
**Fortigate.logout()** Logout from the Fortigate using REST API


send_command()
..............
**Fortigate.delete(url)** Sends show command to the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
cmd             *str*   Show command to send to the Fortigate
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


exist()
.......
**Fortigate.exist(url)** Check does an object exists in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object exist, *<Response [404]>* Object does not exist


get()
.....
**Fortigate.get(url)** GET object configured in the Fortigate.
Fortigate returns dictionary with key="results".

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
=============== ======= ============================================================================

Return
    *List[dict]* of the objects data


get_l()
.......
**Fortigate.get_l(url)** GET list of objects.
Fortigate returns list of items.

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL
=============== ======= ============================================================================

Return
    *List[dict]* of the objects


post()
......
**Fortigate.post(url, data)** POST (create) object in the Fortigate based on the data

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
data            *dict*  Data of the object
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created or already exist in the Fortigate


put()
.....
**Fortigate.put(url, data)** PUT (update) existing object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
data            *dict*  Data of the object
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


----------------------------------------------------------------------------------------------------

SSH
---
**SSH(host, username, password, ssh)**
SSH connector to the Fortigate. Contains methods to get and put configuration commands using ssh.
Note, FortigateAPI parameter "vdom" used in REST API only and not used in SSH.
In order to send cli commands to a specific vdom, you need "config vdom" before.

Python examples `./examples/ssh.py`_

Python examples `./examples/ssh_vdom.py`_

.. code:: python

    from fortigate_api import FortigateAPI

    fgt_api = FortigateAPI(host="host", username="username", password="password")
    fgt_api.ssh.login()

    # Show interface config
    config = fgt_api.ssh.send_command("show system interface dmz")

    # Change interface description from "dmz" to "DMZ"
    cmds = ["config system interface",
            "edit dmz",
            "set description DMZ",
            "end"]
    output = fgt_api.ssh.send_config_set(cmds)


=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
host            *str*   Firewall ip address or hostname
username        *str*   Administrator name
password        *str*   Administrator password
ssh             *dict*  Netmiko *ConnectHandler* parameters
=============== ======= ============================================================================


login()
.......
**SSH.login()** Login to the Fortigate using SSH


logout()
........
**SSH.logout()** Logout from the Fortigate using SSH


send_command()
..............
**SSH.send_command(str, kwargs)** Sends the command to the Fortigate

=============== ============= ======================================================================
Parameter       Type          Description
=============== ============= ======================================================================
cmd             *str*         The command to be executed on the Fortigate
kwargs          *dict*        (optional) Netmiko parameters
=============== ============= ======================================================================

Return
    Output of the command


send_config_set()
.................
**SSH.send_config_set(cmds, kwargs)** Sends configuration commands to the Fortigate

=============== ============= ======================================================================
Parameter       Type          Description
=============== ============= ======================================================================
cmds            *List[str]*   Configuration commands to be executed on the Fortigate
kwargs          *dict*        (optional) Netmiko parameters
=============== ============= ======================================================================

Return
    Output of the commands

----------------------------------------------------------------------------------------------------


.. _`./examples`: ./examples
.. _`./examples/yml`: ./examples/yml
.. _`./examples/yml/address.yml`: ./examples/yml/address.yml
.. _`./examples/yml/address_group.yml`: ./examples/yml/address_group.yml
.. _`./examples/yml/antivirus.yml`: ./examples/yml/antivirus.yml
.. _`./examples/yml/application.yml`: ./examples/yml/application.yml
.. _`./examples/yml/dhcp_server.yml`: ./examples/yml/dhcp_server.yml
.. _`./examples/yml/external_resource.yml`: ./examples/yml/external_resource.yml
.. _`./examples/yml/interface.yml`: ./examples/yml/interface.yml
.. _`./examples/yml/internet_service.yml`: ./examples/yml/internet_service.yml
.. _`./examples/yml/ip_pool.yml`: ./examples/yml/ip_pool.yml
.. _`./examples/yml/policy.yml`: ./examples/yml/policy.yml
.. _`./examples/yml/schedule.yml`: ./examples/yml/schedule.yml
.. _`./examples/yml/service.yml`: ./examples/yml/service.yml
.. _`./examples/yml/service_category.yml`: ./examples/yml/service_category.yml
.. _`./examples/yml/service_group.yml`: ./examples/yml/service_group.yml
.. _`./examples/yml/snmp_community.yml`: ./examples/yml/snmp_community.yml
.. _`./examples/yml/virtual_ip.yml`: ./examples/yml/virtual_ip.yml
.. _`./examples/yml/zone.yml`: ./examples/yml/zone.yml

.. _`./examples/address.py`: ./examples/address.py
.. _`./examples/address_group.py`: ./examples/address_group.py
.. _`./examples/address_token.py`: ./examples/address_token.py
.. _`./examples/dhcp_server.py`: ./examples/dhcp_server.py
.. _`./examples/external_resource.py`: ./examples/external_resource.py
.. _`./examples/fortigate.py`: ./examples/fortigate.py
.. _`./examples/fortigate_token.py`: ./examples/fortigate_token.py
.. _`./examples/interface.py`: ./examples/interface.py
.. _`./examples/ip_pool.py`: ./examples/ip_pool.py
.. _`./examples/monitor.py`: ./examples/monitor.py
.. _`./examples/policy.py`: ./examples/policy.py
.. _`./examples/policy_extended_filter.py`: ./examples/policy_extended_filter.py
.. _`./examples/snmp_community.py`: ./examples/snmp_community.py
.. _`./examples/ssh.py`: ./examples/ssh.py
.. _`./examples/ssh_vdom.py`: ./examples/ssh_vdom.py
