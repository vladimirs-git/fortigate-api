
.. image:: https://img.shields.io/pypi/v/fortigate-api.svg
   :target: https://pypi.python.org/pypi/fortigate-api
.. image:: https://img.shields.io/pypi/pyversions/fortigate-api.svg
   :target: https://pypi.python.org/pypi/fortigate-api

fortigate-api
=============

Python package to configure Fortigate (Fortios) devices using REST API and SSH.
With this package, you can create, delete, get, update any objects in the Fortigate.
The most commonly used `Objects`_ are implemented in the `FortigateAPI`_ methods, but you can
manipulate any other objects that can be accessed through the REST API using the `Fortigate`_
methods. You can also get and change the Fortigate configuration through SSH.

.. contents:: **Contents**
    :local:


Requirements
------------

Python >=3.8


Installation
------------

Install the package from pypi.org release

.. code:: bash

    pip install fortigate-api

or install the package from github.com release

.. code:: bash

    pip install https://github.com/vladimirs-git/fortigate-api/archive/refs/tags/1.0.1.tar.gz

or install the package from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/fortigate-api


Objects
-------
The objects implemented in `FortigateAPI`_.
To get an idea of the objects, you can change the *hostname* in the following URLs and
look it in the Fortigate web management interface. The first URL is for the Web GUI, the second
one is for the REST API. Not all object implemented in `FortigateAPI`_ (only the most used by me),
access to any other objects is available via `Fortigate`_.

=================== ================================================================================
Object              GUI and REST API URL to the object, FortiOS v6.4
=================== ================================================================================
`Address`_          https://hostname/ng/firewall/address
                    https://hostname/api/v2/cmdb/firewall/address/
`AddressGroup`_     https://hostname/ng/firewall/address
                    https://hostname/api/v2/cmdb/firewall/addrgrp/
`Antivirus`_        https://hostname/ng/utm/antivirus/profile
                    https://hostname/api/v2/cmdb/antivirus/profile/
`Application`_      https://hostname/ng/utm/appctrl/sensor
                    https://hostname/api/v2/cmdb/application/list/
`DhcpServer`_       https://hostname/ng/interface/edit/{name}
                    https://hostname/api/v2/cmdb/system.dhcp/server/
`Interface`_        https://hostname/ng/interface
                    https://hostname/api/v2/cmdb/system/interface/
`InternetService`_  https://hostname/ng/firewall/internet_service
                    https://hostname/api/v2/cmdb/firewall/internet-service/
`IpPool`_           https://hostname/ng/firewall/ip-pool
                    https://hostname/api/v2/cmdb/firewall/ippool/
`Policy`_           https://hostname/ng/firewall/policy/policy/standard
                    https://hostname/api/v2/cmdb/firewall/policy/
`Schedule`_         https://hostname/ng/firewall/schedule
                    https://hostname/api/v2/cmdb/firewall.schedule/onetime/
`Service`_          https://hostname/ng/firewall/service
                    https://hostname/api/v2/cmdb/firewall.service/custom/
`ServiceCategory`_  https://hostname/ng/firewall/service
                    https://hostname/api/v2/cmdb/firewall.service/category/
`ServiceGroup`_     https://hostname/ng/firewall/service
                    https://hostname/api/v2/cmdb/firewall.service/group/
`SnmpCommunity`_    https://hostname/ng/system/snmp
                    https://hostname/api/v2/cmdb/system.snmp/community/
`VirtualIp`_        https://hostname/ng/firewall/virtual-ip
                    https://hostname/api/v2/cmdb/firewall/vip/
`Zone`_             https://hostname/ng/interface
                    https://hostname/api/v2/cmdb/system/zone/
=================== ================================================================================


FortigateAPI
------------
**FortigateAPI(host, username, password, scheme, port, timeout, vdom)**
Set of methods for working with the most commonly used `Objects`_.
Code usage examples in *./examples/examples.py*

=============== ======= ============================================================================
Parameter        Type    Description
=============== ======= ============================================================================
host            *str*   Firewall ip address or hostname
username        *str*   Administrator name
password        *str*   Administrator password
scheme          *str*   (optional) "https" (default) or "http"
port            *int*   (optional) TCP port, by default 443 for "https", 80 for "http"
timeout         *int*   (optional) Session timeout minutes (default 15)
verify          *str*   (optional) Enable SSL certificate verification for HTTPS requests. True -  enable, False - disable (default)
vdom            *str*   Name of virtual domain (default "root")
=============== ======= ============================================================================



Address
-------
FortiOS v6.4 data example `./examples/yml/address.yml`_


create()
........
**FortigateAPI.address.create(data)**
Creates address-object in the Fortigate.

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
Deletes address-object from the Fortigate.
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Unique identifier. Name of the address-object. Used to delete a single object
filter          *str*, *List[str]*  Filters address-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than returns *<Response [200]>*
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


Examples
........

Address examples:

- Creates address in the Fortigate
- Gets all addresses from the Fortigate
- Gets filtered address by name (unique identifier)
- Filters address by operator *equals* "=="
- Filters address by operator *contains* "=@"
- Filters address by operator *not equals* "!="
- Updates address data in the Fortigate
- Checks for presence of address in the Fortigate
- Deletes address from the Fortigate by name
- Deletes addresses from the Fortigate by filter
- Checks for absence of address in the Fortigate
- FortigateAPI *with* statement

`./examples/address.py`_



AddressGroup
------------
FortiOS v6.4 data example `./examples/yml/address_group.yml`_


create()
........
**FortigateAPI.address_group.create(data)**
Creates address-group-object in the Fortigate

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
Deletes address-group-object from the Fortigate
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Name of the address-group-object (unique identifier). Used to delete a single object
filter          *str*, *List[str]*  Filters address-group-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than returns *<Response [200]>*
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


Examples
........
AddressGroup examples:

- Creates address-group in the Fortigate
- Gets all address-groups from the Fortigate
- Gets filtered address-group by name (unique identifier)
- Filters address-group by operator *equals* "=="
- Filters address-group by operator *contains* "=@"
- Filters address-group by operator *not equals* "!="
- Updates address-group data in the Fortigate
- Checks for presence of address-group in the Fortigate
- Deletes address-group from the Fortigate by name
- Deletes address-groups from the Fortigate by filter
- Checks for absence of address-group in the Fortigate

`./examples/address_group.py`_



Antivirus
---------
**Antivirus** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/antivirus.yml`_

**FortigateAPI.antivirus.create(data)**

**FortigateAPI.antivirus.delete(uid, filter)**

**FortigateAPI.antivirus.get(uid, filter)**

**FortigateAPI.antivirus.is_exist(uid)**

**FortigateAPI.antivirus.update(data, uid)**



Application
-----------
**Application** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/application.yml`_

**FortigateAPI.application.create(data)**

**FortigateAPI.application.delete(uid, filter)**

**FortigateAPI.application.get(uid, filter)**

**FortigateAPI.application.is_exist(uid)**

**FortigateAPI.antivirus.update(data, uid)**



DhcpServer
----------
**DhcpServer** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/dhcp_server.yml`_

**FortigateAPI.dhcp_server.create(data)** Note, in Fortigate is possible to create multiple DHCP servers with the same settings, you need control duplicates

**FortigateAPI.dhcp_server.delete(uid, filter)**

**FortigateAPI.dhcp_server.get(uid, filter)**

**FortigateAPI.dhcp_server.is_exist(uid)**

**FortigateAPI.dhcp_server.update(data, uid)**

DhcpServer examples `./examples/dhcp_server.py`_



Interface
---------
**Interface** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/interface.yml`_

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


Examples
........
Interface examples:

- Gets all interfaces in vdom "root" from the Fortigate
- Gets filtered interface by name (unique identifier)
- Filters interface by operator *equals* "=="
- Filters interface by operator contains "=@"
- Filters interface by operator *not equals* "!="
- Filters interface by multiple conditions
- Updates interface data in the Fortigate
- Checks for presence of interface in the Fortigate
- Gets all interfaces in vdom "VDOM"

`./examples/interface.py`_



InternetService
---------------
**InternetService** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/internet_service.yml`_

**FortigateAPI.internet_service.create(data)**

**FortigateAPI.internet_service.delete(uid, filter)**

**FortigateAPI.internet_service.get(uid, filter)**

**FortigateAPI.internet_service.is_exist(uid)**

**FortigateAPI.internet_service.update(data, uid)**



IpPool
------
**IpPool** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/ip_pool.yml`_

**FortigateAPI.ip_pool.create(data)**

**FortigateAPI.ip_pool.delete(uid, filter)**

**FortigateAPI.ip_pool.get(uid, filter)**

**FortigateAPI.ip_pool.is_exist(uid)**

**FortigateAPI.ip_pool.update(data, uid)**



Policy
------
FortiOS v6.4 data example `./examples/yml/policy.yml`_


create()
........
**FortigateAPI.policy.create(data)**
Creates policy-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the policy-object
=============== ======= ============================================================================

Return
    Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created in the Fortigate


delete()
........
Deletes policy-object from the Fortigate
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*, *int*        Identifier of the policy-object. Used to delete a single object
filter          *str*, *List[str]*  Filters policy-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than returns *<Response [200]>*
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


Examples
........
Policy examples:

- Creates policy in the Fortigate
- Gets all policies from the Fortigate
- Gets filtered policy by policyid (unique identifier)
- Filters policies by name, by operator *equals* "=="
- Filters policies by operator *contains* "=@"
- Filters policies by operator *not equals* "!="
- Updates policy data in the Fortigate
- Checks for presence of policy in the Fortigate
- Gets all policies with destination address == "192.168.1.2/32"
- Deletes policy from the Fortigate by policyid (unique identifier)
- Deletes policies from the Fortigate by filter (by name)
- Checks for absence of policy in the Fortigate

`./examples/policy.py`_


Policy Extended Filter examples:

- Gets the rules where source prefix is equals 127.0.1.0/30
- Gets the rules where source prefix is not equals 127.0.1.0/30
- Gets the rules where source addresses are in subnets of 127.0.1.0/24
- Gets the rules where source prefixes are supernets of address 127.0.1.1/32
- Gets the rules where source prefix are equals 127.0.1.0/30 and destination prefix are equals 127.0.2.0/30
- Delete policy, address-group, addresses from the Fortigate (order is important)

`./examples/policy_extended_filter.py`_



Schedule
--------
**Schedule** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/schedule.yml`_

**FortigateAPI.schedule.create(data)**

**FortigateAPI.schedule.delete(uid, filter)**

**FortigateAPI.schedule.get(uid, filter)**

**FortigateAPI.schedule.is_exist(uid)**

**FortigateAPI.schedule.update(data, uid)**



Service
-------
**Service** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service.yml`_

**FortigateAPI.service.create(data)**

**FortigateAPI.service.delete(uid, filter)**

**FortigateAPI.service.get(uid, filter)**

**FortigateAPI.service.is_exist(uid)**

**FortigateAPI.service.update(data, uid)**



ServiceCategory
---------------
**ServiceCategory** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service_category.yml`_

**FortigateAPI.service_category.create(data)**

**FortigateAPI.service_category.delete(uid, filter)**

**FortigateAPI.service_category.get(uid, filter)**

**FortigateAPI.service_category.is_exist(uid)**

**FortigateAPI.service_category.update(data, uid)**



ServiceGroup
------------
**ServiceGroup** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service_group.yml`_

**FortigateAPI.service_group.create(data)**

**FortigateAPI.service_group.delete(uid, filter)**

**FortigateAPI.service_group.get(uid, filter)**

**FortigateAPI.service_group.is_exist(uid)**

**FortigateAPI.service_group.update(data, uid)**



SnmpCommunity
-------------
**SnmpCommunity**

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


Examples
........
SnmpCommunity examples `./examples/snmp_community.py`_



VirtualIP
---------
**VirtualIP** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/virtual_ip.yml`_

**FortigateAPI.virtual_ip.create(data)**

**FortigateAPI.virtual_ip.delete(uid, filter)**

**FortigateAPI.virtual_ip.get(uid, filter)**

**FortigateAPI.virtual_ip.is_exist(uid)**

**FortigateAPI.virtual_ip.update(data, uid)**



Zone
----
**Zone** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/zone.yml`_

**FortigateAPI.zone.create(data)**

**FortigateAPI.zone.delete(uid, filter)**

**FortigateAPI.zone.get(uid, filter)**

**FortigateAPI.zone.is_exist(uid)**

**FortigateAPI.zone.update(data, uid)**



Fortigate
---------
**Fortigate(host, username, password, scheme, port, timeout, vdom)**
REST API connector to the Fortigate. Contains generic methods (get, put, delete, etc.)
to work with any objects available through the REST API. `Fortigate`_ is useful for working with
objects that are not implemented in `FortigateAPI`_

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
host            *str*   Firewall ip address or hostname
username        *str*   Administrator name
password        *str*   Administrator password
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
**Fortigate.get(url)** GET object configured in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
=============== ======= ============================================================================

Return
    *List[dict]* of the objects data


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


Examples
........
Fortigate examples:

- Creates address in the Fortigate
- Gets address data from the Fortigate
- Updates address data in the Fortigate
- Checks for presence of address in the Fortigate
- Deletes address from the Fortigate
- Checks for absence of address in the Fortigate
- Fortigate *with* statement

`./examples/fortigate.py`_



SSH
---
**SSH(host, username, password, ssh)**
SSH connector to the Fortigate. Contains methods to get and put configuration commands using ssh.

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


Examples
........
SSH examples:

- Show interface config
- Change interface description from "dmz" to "DMZ"
- Check interface description is changed
- Change read-timeout timer for long awaited commands

`./examples/ssh.py`_



.. _`./examples/yml/address.yml`: ./examples/yml/address.yml
.. _`./examples/yml/address_group.yml`: ./examples/yml/address_group.yml
.. _`./examples/yml/antivirus.yml`: ./examples/yml/antivirus.yml
.. _`./examples/yml/application.yml`: ./examples/yml/application.yml
.. _`./examples/yml/dhcp_server.yml`: ./examples/yml/dhcp_server.yml
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
.. _`./examples/dhcp_server.py`: ./examples/dhcp_server.py
.. _`./examples/fortigate.py`: ./examples/fortigate.py
.. _`./examples/interface.py`: ./examples/interface.py
.. _`./examples/policy.py`: ./examples/policy.py
.. _`./examples/policy_extended_filter.py`: ./examples/policy_extended_filter.py
.. _`./examples/snmp_community.py`: ./examples/snmp_community.py
.. _`./examples/ssh.py`: ./examples/ssh.py