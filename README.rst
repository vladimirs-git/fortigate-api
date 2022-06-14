fortigate-api
=============

Python package for configuring Fortigate (Fortios) devices using REST API.
With this package, you can create, delete, get, update any objects in the Fortigate.
The most commonly used `Objects`_ are implemented in the `FortigateAPI`_ methods, but you can
manipulate any other objects that can be accessed through the REST API using the `Fortigate`_ methods.

.. contents::

.. sectnum::


Installation
------------

Install the package from pypi.org release

.. code:: bash

    pip install fortigate-api

or install the package from github.com release

.. code:: bash

    pip install https://github.com/vladimirs-git/fortigate-api/archive/refs/tags/0.2.3.tar.gz

or install the package from github.com repository

.. code:: bash

    pip install git+https://github.com/vladimirs-git/fortigate-api


Objects
-------
The objects implemented in `FortigateAPI`_.
To get an idea of the objects, change *hostname* in the following URLs and
look it in Fortigate web management interface.
The first URL is for the Web GUI, the second one is for the REST API.

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
`Interface`_        https://hostnae/ng/interface
					https://hostname/api/v2/cmdb/system/interface/
`InternetService`_  https://hostnae/ng/firewall/internet_service
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
`Zone`_             https://hostnae/ng/interface
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
scheme          *str*   "https" or "http", by default "https"
port            *int*   TCP port, by default 443 for "https", 80 for "http"
timeout         *int*   Session timeout (minutes), by default 15
vdom            *str*   Name of virtual domain, by default "root"
=============== ======= ============================================================================


Address
-------
FortiOS v6.4 data example `./examples/yml/address.yml`_


create(data)
............
**FortigateAPI.address.create(data)**
Creates address-object in the Fortigate.

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the address-object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created in the Fortigate


delete(uid, filter)
...................
**FortigateAPI.address.delete(uid, filter)**
Deletes address-object from Fortigate.
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Unique identifier. Name of the address-object. Used to delete a single object
filter          *str*, *List[str]*  Filters address-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than returns *<Response [200]>*
=============== =================== ================================================================

Return
	Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


get(uid, filter)
................
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


is_exist(uid)
.............
**FortigateAPI.address.is_exist(uid)**
Checks does an address-object exists in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
uid             *str*   Name of the address-object (unique identifier)
=============== ======= ============================================================================

Return
	*bool* True - object exist, False - object does not exist


update(uid, data)
............
**FortigateAPI.address.update(uid, data)**
Updates address-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
uid             *str*   Name of the address-object
data            *dict*  Data of the address-object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


Examples - Address
..................
- Creates address in the Fortigate
- Gets all addresses from Fortigate
- Gets filtered address by name (unique identifier)
- Filters address by operator *equals* "=="
- Filters address by operator *contains* "=@"
- Filters address by operator *not equals* "!="
- Updates address data in the Fortigate
- Checks for presence of address in the Fortigate
- Deletes address from Fortigate by name
- Deletes addresses from Fortigate by filter
- Checks for absence of address in the Fortigate

.. code:: python

	from pprint import pprint
	from fortigate_api import FortigateAPI

	fgt = FortigateAPI(host="host", username="username", password="password")
	fgt.login()

	# Creates address in the Fortigate
	data = {"name": "ADDRESS",
			"obj-type": "ip",
			"subnet": "127.0.0.100 255.255.255.252",
			"type": "ipmask"}
	response = fgt.address.create(data=data)
	print("address.create", response)  # address.create <Response [200]>

	# Gets all addresses from Fortigate
	addresses = fgt.address.get()
	print("addresses count", len(addresses))  # addresses count 1727

	# Gets filtered address by name (unique identifier)
	addresses = fgt.address.get(uid="ADDRESS")
	pprint(addresses)
	#  [{"comment": "",
	#    "name": "ADDRESS",
	#    "subnet": "127.0.0.100 255.255.255.252",
	#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
	#    ...
	#    }]

	# Filters address by operator equals "=="
	addresses = fgt.address.get(filter="name==ADDRESS")
	print("addresses count", len(addresses))  # addresses count 1

	# Filters address by operator contains "=@"
	addresses = fgt.address.get(filter="subnet=@127.0")
	print("addresses count", len(addresses))  # addresses count 4

	# Filters address by operator not equals "!="
	addresses = fgt.address.get(filter="name!=ADDRESS")
	print("addresses count", len(addresses))  # addresses count 1726

	# Filters address by multiple conditions
	addresses = fgt.address.get(filter=["subnet=@127.0", "type==ipmask"])
	print("addresses count", len(addresses))  # addresses count 1

	# Updates address data in the Fortigate
	data = dict(name="ADDRESS", subnet="127.0.0.255 255.255.255.255", color=6)
	response = fgt.address.update(uid="ADDRESS", data=data)
	print("address.update", response, response.ok)  # address.update <Response [200]> True

	# Checks for presence of address in the Fortigate
	response = fgt.address.is_exist(uid="ADDRESS")
	print("address.is_exist", response)  # address.is_exist True

	# Deletes address from Fortigate by name
	response = fgt.address.delete(uid="ADDRESS")
	print("address.delete", response, response.ok)  # address.delete <Response [200]> True

	# Deletes addresses from Fortigate by filter (address was deleted before)
	response = fgt.address.delete(filter="name=@ADDRESS")
	print("address.delete", response, response.ok)  # address.delete <Response [500]> False

	# Checks for absence of address in the Fortigate
	response = fgt.address.is_exist(uid="ADDRESS")
	print("address.is_exist", response)  # address.is_exist False

	fgt.logout()


AddressGroup
------------
FortiOS v6.4 data example `./examples/yml/address_group.yml`_

create(data)
............
**FortigateAPI.address_group.create(data)**
Creates address-group-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the address-group-object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created in the Fortigate


delete(uid, filter)
...................
**FortigateAPI.address_group.delete(uid, filter)**
Deletes address-group-object from Fortigate
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*               Name of the address-group-object (unique identifier). Used to delete a single object
filter          *str*, *List[str]*  Filters address-group-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than returns *<Response [200]>*
=============== =================== ================================================================

Return
	Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


get(uid, filter)
................
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


is_exist(uid)
.............
**FortigateAPI.address_group.is_exist(uid)**
Checks does an address-group-object exists in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
uid             *str*   Name of the address-group-object (unique identifier)
=============== ======= ============================================================================

Return
	*bool* True - object exist, False - object does not exist


update(uid, data)
............
**FortigateAPI.address_group.update(uid, data)**
Updates address-group-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
uid             *str*   Name of the address-group-object
data            *dict*  Data of the address-group-object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


Examples - AddressGroup
.......................
- Creates address-group in the Fortigate
- Gets all address-groups from Fortigate
- Gets filtered address-group by name (unique identifier)
- Filters address-group by operator *equals* "=="
- Filters address-group by operator *contains* "=@"
- Filters address-group by operator *not equals* "!="
- Updates address-group data in the Fortigate
- Checks for presence of address-group in the Fortigate
- Deletes address-group from Fortigate by name
- Deletes address-groups from Fortigate by filter
- Checks for absence of address-group in the Fortigate

.. code:: python

	from pprint import pprint
	from fortigate_api import FortigateAPI

	fgt = FortigateAPI(host="host", username="username", password="password")
	fgt.login()

	# Creates address and address-group in the Fortigate
	data = {"name": "ADDRESS",
			"obj-type": "ip",
			"subnet": "127.0.0.100 255.255.255.255",
			"type": "ipmask"}
	response = fgt.address.create(data=data)
	print("address.create", response)  # address.create <Response [200]>
	data = {"name": "ADDR_GROUP", "member": [{"name": "ADDRESS"}]}
	response = fgt.address_group.create(data=data)
	print("address_group.creat", response)  # address_group.creat <Response [200]>

	# Gets all address-groups from Fortigate
	address_groups = fgt.address_group.get()
	print("address_groups count", len(address_groups))  # address_groups count 115

	# Gets filtered address_group by name (unique identifier)
	address_groups = fgt.address_group.get(uid="ADDR_GROUP")
	pprint(address_groups)
	#  [{"comment": "",
	#    "name": "ADDR_GROUP",
	#    "member": [{"name": "ADDRESS", "q_origin_key": "ADDRESS"}],
	#    "uuid": "d346aeca-d76a-51ec-7005-541cf3b816f5",
	#    ...
	#    }]

	# Filters address_group by operator equals "=="
	address_groups = fgt.address_group.get(filter="name==ADDR_GROUP")
	print("address_groups count", len(address_groups))  # address_groups count 1

	# Filters address_group by operator contains "=@"
	address_groups = fgt.address_group.get(filter="name=@MS")
	print("address_groups count", len(address_groups))  # address_groups count 6

	# Filters address_group by operator not equals "!="
	address_groups = fgt.address_group.get(filter="name!=ADDR_GROUP")
	print("address_groups count", len(address_groups))  # address_groups count 114

	# Filters address_group by multiple conditions
	address_groups = fgt.address_group.get(filter=["name=@MS", "color==6"])
	print("address_groups count", len(address_groups))  # address_groups count 2

	# Updates address_group data in the Fortigate
	data = dict(name="ADDR_GROUP", color=6)
	response = fgt.address_group.update(uid="ADDR_GROUP", data=data)
	print("address_group.update", response)  # address_group.update <Response [200]>

	# Checks for presence of address_group in the Fortigate
	response = fgt.address_group.is_exist(uid="ADDR_GROUP")
	print("address_group.is_exist", response)  # address_group.is_exist True

	# Deletes address_group from Fortigate by name
	response = fgt.address_group.delete(uid="ADDR_GROUP")
	print("address_group.delete", response)  # address_group.delete <Response [200]>

	# Deletes address_groups by filter by filter
	response = fgt.address_group.delete(filter="name=@ADDR_GROUP")
	print("address_group.delete", response)  # address_group.delete <Response [200]>

	# Deletes address object
	response = fgt.address.delete(uid="ADDRESS")
	print("address.delete", response)  # address.delete <Response [200]>

	# Checks for absence of address_group in the Fortigate
	response = fgt.address_group.is_exist(uid="ADDR_GROUP")
	print("address_group.is_exist", response)  # address_group.is_exist False

	fgt.logout()


Antivirus
---------
**Antivirus** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/antivirus.yml`_

**FortigateAPI.antivirus.create(data)**

**FortigateAPI.antivirus.delete(uid, filter)**

**FortigateAPI.antivirus.get(uid, filter)**

**FortigateAPI.antivirus.is_exist(uid)**

**FortigateAPI.antivirus.update(uid, data)**


Application
-----------
**Application** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/application.yml`_

**FortigateAPI.application.create(data)**

**FortigateAPI.application.delete(uid, filter)**

**FortigateAPI.application.get(uid, filter)**

**FortigateAPI.application.is_exist(uid)**

**FortigateAPI.antivirus.update(uid, data)**


Interface
---------
**Interface** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/interface.yml`_

**FortigateAPI.interface.create(data)**

**FortigateAPI.interface.delete(uid, filter)**

get(uid, filter, all)
.....................
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

**FortigateAPI.interface.update(uid, data)**


Examples - Interface
....................
- Gets all interfaces in vdom "root" from Fortigate
- Gets filtered interface by name (unique identifier)
- Filters interface by operator *equals* "=="
- Filters interface by operator contains "=@"
- Filters interface by operator *not equals* "!="
- Filters interface by multiple conditions
- Updates interface data in the Fortigate
- Checks for presence of interface in the Fortigate
- Gets all interfaces in vdom "VDOM"

.. code:: python

	from pprint import pprint
	from fortigate_api import FortigateAPI

	fgt = FortigateAPI(host="host", username="username", password="password")
	fgt.login()

	# Gets all interfaces in vdom "root" from Fortigate
	interfaces = fgt.interface.get()
	print("interfaces count", len(interfaces))  # interfaces count 21

	# Gets filtered interface by name (unique identifier)
	interfaces = fgt.interface.get(uid="dmz")
	pprint(interfaces)
	#  [{"name": "dmz",
	#    "ip": "0.0.0.0 0.0.0.0",
	#    ...
	#    }]

	# Filters interface by operator equals "=="
	interfaces = fgt.interface.get(filter="name==dmz")
	print("interfaces count", len(interfaces))  # interfaces count 1

	# Filters interface by operator contains "=@"
	interfaces = fgt.interface.get(filter="name=@wan")
	print("interfaces count", len(interfaces))  # interfaces count 2

	# Filters interface by operator not equals "!="
	interfaces = fgt.interface.get(filter="name!=dmz")
	print("interfaces count", len(interfaces))  # interfaces count 20

	# Filters interface by multiple conditions
	interfaces = fgt.interface.get(filter=["allowaccess=@ping", "detectprotocol==ping"])
	print("interfaces count", len(interfaces))  # interfaces count 8

	# Updates interface data in the Fortigate
	data = dict(name="dmz", description="dmz")
	response = fgt.interface.update(uid="dmz", data=data)
	print("interface.update", response)  # interface.update <Response [200]>

	# Checks for presence of interface in the Fortigate
	response = fgt.interface.is_exist(uid="dmz")
	print("interface.is_exist", response)  # interface.is_exist True

	# Changes virtual domain to "VDOM" and gets all interfaces inside this vdom
	fgt.fgt.vdom = "VDOM"
	print(f"{fgt!r}")
	# Fortigate(host='host', username='username', password='********', vdom='VDOM')
	interfaces = fgt.interface.get()
	print("interfaces count", len(interfaces))  # interfaces count 0
	fgt.vdom = "root"
	print(f"{fgt!r}")
	# Fortigate(host='host', username='username', password='********')

	fgt.logout()


InternetService
---------------
**InternetService** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/internet_service.yml`_

**FortigateAPI.internet_service.create(data)**

**FortigateAPI.internet_service.delete(uid, filter)**

**FortigateAPI.internet_service.get(uid, filter)**

**FortigateAPI.internet_service.is_exist(uid)**

**FortigateAPI.internet_service.update(uid, data)**


IpPool
------
**IpPool** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/ip_pool.yml`_

**FortigateAPI.ip_pool.create(data)**

**FortigateAPI.ip_pool.delete(uid, filter)**

**FortigateAPI.ip_pool.get(uid, filter)**

**FortigateAPI.ip_pool.is_exist(uid)**

**FortigateAPI.ip_pool.update(uid, data)**


Policy
------
FortiOS v6.4 data example `./examples/yml/policy.yml`_

create(data)
............
**FortigateAPI.policy.create(data)**
Creates policy-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the policy-object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created in the Fortigate


delete(uid, filter)
...................
Deletes policy-object from Fortigate
Only one of the parameters *uid* or *filter* can be used in the same time.

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*, *int*        Identifier of the policy-object. Used to delete a single object
filter          *str*, *List[str]*  Filters policy-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to delete multiple objects. *Response* with the highest *status_code* (most important error) will be returned. If no address-objects was found and deleted than returns *<Response [200]>*
=============== =================== ================================================================

Return
	Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


get(uid, filter, efilter)
.........................
**FortigateAPI.policy.get(uid, filter)**
Gets policy-objects, all or filtered by some of params.
Only one of the parameters *uid* or *filter* can be used in the same time.
The parameter *efilter* can be combined with "srcaddr", "srcaddr", *filter*

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*, *int*        Filters policy-object by policyid (unique identifier). Used to get a single object
filter          *str*, *List[str]*  Filters policy-objects by one or multiple conditions: equals "==", not equals "!=", contains "=@". Used to get multiple objects
efilter         *str*, *List[str]*  Extended filter: "srcaddr", "dstaddr" by condition: equals "==", not equals "!=",  supernets ">=", subnets "<=". Using this option, you can search for rules by subnets and supernets that are configured in Addresses and AddressGroups. See the examples `Examples - Policy extended filter`_ for details.
=============== =================== ================================================================

Return
	*List[dict]* List of policy-objects

is_exist(uid)
.............
**FortigateAPI.policy.is_exist(uid)** Checks does an policy-object exists in the Fortigate

=============== =================== ================================================================
Parameter       Type                Description
=============== =================== ================================================================
uid             *str*, *int*        Identifier of the policy-object
=============== =================== ================================================================

Return
	*bool* True - object exist, False - object does not exist

move(uid, position, neighbor)
.............................
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

update(uid, data)
............
**FortigateAPI.policy.update(uid, data)** Updates policy-object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
data            *dict*  Data of the policy-object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated

Examples - Policy
.................
- Creates policy in the Fortigate
- Gets all policies from Fortigate
- Gets filtered policy by policyid (unique identifier)
- Filters policies by name, by operator *equals* "=="
- Filters policies by operator *contains* "=@"
- Filters policies by operator *not equals* "!="
- Updates policy data in the Fortigate
- Checks for presence of policy in the Fortigate
- Gets all policies with destination address == "192.168.1.2/32"
- Deletes policy from Fortigate by policyid (unique identifier)
- Deletes policies from Fortigate by filter (by name)
- Checks for absence of policy in the Fortigate

.. code:: python

	from pprint import pprint
	from fortigate_api import FortigateAPI

	fgt = FortigateAPI(host="host", username="username", password="password")
	fgt.login()

	# Creates policy in the Fortigate
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
	response = fgt.policy.create(data=data)
	print("policy.create", response)  # policy.create <Response [200]>

	# Gets all policies from Fortigate
	policies = fgt.policy.get()
	print("policies count", len(policies))  # policies count 244

	# Gets filtered policy by policyid (unique identifier)
	policies = fgt.policy.get(uid="POLICY")
	pprint(policies)
	#  [{"name": "POLICY",
	#    "policyid": 323,
	#    "uuid": "521390dc-d771-51ec-9dc2-32467e1bc561",
	#    ...
	#    }]

	# Filters policies by name, by operator equals "=="
	policies = fgt.policy.get(filter="name==POLICY")
	print("policies count", len(policies))  # policies count 1
	policyid = policies[0]["policyid"]
	print("policyid", policyid)  # policyid 323

	# Filters policies by operator contains "=@"
	policies = fgt.policy.get(filter="name=@POL")
	print("policies count", len(policies))  # policies count 6

	# Filters policies by operator not equals "!="
	policies = fgt.policy.get(filter="name!=POLICY")
	print("policies count", len(policies))  # policies count 243

	# Filters policies by multiple conditions
	policies = fgt.policy.get(filter=["name=@POL", "color==6"])
	print("policies count", len(policies))  # policies count 2

	# Updates policy data in the Fortigate
	data = dict(policyid=policyid, status="disable")
	response = fgt.policy.update(uid="POLICY", data=data)
	print("policy.update", response)  # policy.update <Response [200]>

	# Checks for presence of policy in the Fortigate
	response = fgt.policy.is_exist(uid=policyid)
	print("policy.is_exist", response)  # policy.is_exist True

	# Gets all policies with destination address == "192.168.1.2/32"
	policies = []
	addresses = fgt.address.get(filter="subnet==192.168.1.2 255.255.255.255")
	for policy in fgt.policy.get():
		dstaddr = [d["name"] for d in policy["dstaddr"]]
		for address in addresses:
			if address["name"] in dstaddr:
				policies.append(policy)
	print("policies count", len(policies))  # policies count 2

	# Moves policy to top
	neighbor = fgt.policy.get()[0]
	response = fgt.policy.move(uid=policyid, position="before", neighbor=neighbor["policyid"])
	print("policy.move", response, response.ok)  # policy.move <Response [200]> False

	# Deletes policy from Fortigate by policyid (unique identifier)
	response = fgt.policy.delete(uid=policyid)
	print("policy.delete", response, response.ok)  # policy.delete <Response [200]> True

	# Deletes policies from Fortigate by filter (by name)
	response = fgt.policy.delete(filter="name==POLICY")
	print("policy.delete", response, response.ok)  # policy.delete <Response [200]> True

	# Checks for absence of policy in the Fortigate
	response = fgt.policy.is_exist(uid=policyid)
	print("policy.is_exist", response)  # policy.is_exist False

	fgt.logout()

Examples - Policy extended filter
.................................
- Gets the rules where source prefix is equals 127.0.1.0/30
- Gets the rules where source prefix is not equals 127.0.1.0/30
- Gets the rules where source addresses are in subnets of 127.0.1.0/24
- Gets the rules where source prefixes are supernets of address 127.0.1.1/32
- Gets the rules where source prefix are equals 127.0.1.0/30 and destination prefix are equals 127.0.2.0/30
- Delete policy, address-group, addresses from Fortigate (order is important)

.. code:: python

	from pprint import pprint
	from fortigate_api import FortigateAPI

	fgt = FortigateAPI(host="host", username="username", password="password")
	fgt.login()

	# Creates address and address_groupin the Fortigate
	data = {"name": "ADDRESS1",
			"obj-type": "ip",
			"subnet": "127.0.1.0 255.255.255.252",
			"type": "ipmask"}
	response = fgt.address.create(data=data)
	print("address.create", response)  # post <Response [200]>
	data = {"name": "ADDRESS2",
			"obj-type": "ip",
			"subnet": "127.0.2.0 255.255.255.252",
			"type": "ipmask"}
	response = fgt.address.create(data=data)
	print("address.create", response)  # post <Response [200]>
	data = {"name": "ADDR_GROUP", "member": [{"name": "ADDRESS2"}]}
	response = fgt.address_group.create(data=data)
	print("address_group.create", response)  # post <Response [200]>

	# Creates policy in the Fortigate
	data = dict(
		name="POLICY",
		status="enable",
		action="accept",
		srcintf=[{"name": "any"}],
		dstintf=[{"name": "any"}],
		srcaddr=[{"name": "ADDRESS1"}],
		dstaddr=[{"name": "ADDR_GROUP"}],
		service=[{"name": "ALL"}],
		schedule="always",
	)
	response = fgt.policy.create(data=data)
	print("policy.create", response)  # post <Response [200]>

	# Gets the rules where source prefix is equals 127.0.1.0/30
	efilter = "srcaddr==127.0.1.0/30"
	policies = fgt.policy.get(efilter=efilter)
	print(f"{efilter=}", len(policies))  # efilter='srcaddr==127.0.1.0/30' 1

	# Gets the rules where source prefix is not equals 127.0.1.0/30
	efilter = "srcaddr!=127.0.1.0/30"
	policies = fgt.policy.get(efilter=efilter)
	print(f"{efilter=}", len(policies))  # efilter='srcaddr!=127.0.1.0/30' 35

	# Gets the rules where source addresses are in subnets of 127.0.1.0/24
	efilter = "srcaddr<=127.0.1.0/24"
	policies = fgt.policy.get(efilter=efilter)
	print(f"{efilter=}", len(policies))  # efilter='srcaddr<=127.0.1.0/24' 1

	# Gets the rules where source prefixes are supernets of address 127.0.1.1/32
	efilter = "srcaddr>=127.0.1.1/32"
	policies = fgt.policy.get(efilter=efilter)
	print(f"{efilter=}", len(policies))  # efilter='srcaddr>=127.0.1.1/32' 7

	# Gets the rules where source prefix are equals 127.0.1.0/30 and destination prefix are equals 127.0.2.0/30
	efilters = ["srcaddr==127.0.1.0/30", "dstaddr==127.0.2.0/30"]
	policies = fgt.policy.get(efilter=efilters)
	print(f"{efilters=}",
		  len(policies))  # efilters=['srcaddr==127.0.1.0/30', 'dstaddr==127.0.2.0/30'] 1

	# Delete policy, address-group, addresses from Fortigate (order is important)
	response = fgt.address.delete(uid="ADDRESS1")
	print("address.delete", response.ok)  # address.delete <Response [200]>
	response = fgt.policy.delete(filter="name==POLICY")
	print("policy.delete", response.ok)  # policy.delete <Response [200]>
	response = fgt.address_group.delete(uid="ADDR_GROUP")
	print("address_group.delete", response.ok)  # address_group.delete <Response [200]>
	response = fgt.address.delete(uid="ADDRESS1")
	print("address.delete", response.ok)  # address.delete <Response [200]>
	response = fgt.address.delete(uid="ADDRESS2")
	print("address.delete", response.ok)  # address.delete <Response [200]>

	fgt.logout()


Schedule
--------
**Schedule** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/schedule.yml`_

**FortigateAPI.schedule.create(data)**

**FortigateAPI.schedule.delete(uid, filter)**

**FortigateAPI.schedule.get(uid, filter)**

**FortigateAPI.schedule.is_exist(uid)**

**FortigateAPI.schedule.update(uid, data)**


Service
-------
**Service** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service.yml`_

**FortigateAPI.service.create(data)**

**FortigateAPI.service.delete(uid, filter)**

**FortigateAPI.service.get(uid, filter)**

**FortigateAPI.service.is_exist(uid)**

**FortigateAPI.service.update(uid, data)**


ServiceCategory
---------------
**ServiceCategory** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service_category.yml`_

**FortigateAPI.service_category.create(data)**

**FortigateAPI.service_category.delete(uid, filter)**

**FortigateAPI.service_category.get(uid, filter)**

**FortigateAPI.service_category.is_exist(uid)**

**FortigateAPI.service_category.update(uid, data)**


ServiceGroup
------------
**ServiceGroup** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/service_group.yml`_

**FortigateAPI.service_group.create(data)**

**FortigateAPI.service_group.delete(uid, filter)**

**FortigateAPI.service_group.get(uid, filter)**

**FortigateAPI.service_group.is_exist(uid)**

**FortigateAPI.service_group.update(uid, data)**


SnmpCommunity
-------------
**SnmpCommunity**

FortiOS v6.4 data example `./examples/yml/snmp_community.yml`_
**FortigateAPI.snmp_community.create(data)**

**FortigateAPI.snmp_community.delete(uid, filter)**

**FortigateAPI.snmp_community.get(uid, filter)**

**FortigateAPI.snmp_community.is_exist(uid)**

**FortigateAPI.snmp_community.update(uid, data)**


VirtualIP
---------
**VirtualIP** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/virtual_ip.yml`_

**FortigateAPI.virtual_ip.create(data)**

**FortigateAPI.virtual_ip.delete(uid, filter)**

**FortigateAPI.virtual_ip.get(uid, filter)**

**FortigateAPI.virtual_ip.is_exist(uid)**

**FortigateAPI.virtual_ip.update(uid, data)**


Zone
----
**Zone** object has the same parameters and methods as `Address`_

FortiOS v6.4 data example `./examples/yml/zone.yml`_

**FortigateAPI.zone.create(data)**

**FortigateAPI.zone.delete(uid, filter)**

**FortigateAPI.zone.get(uid, filter)**

**FortigateAPI.zone.is_exist(uid)**

**FortigateAPI.zone.update(uid, data)**


Fortigate
---------
**Fortigate(host, username, password, scheme, port, timeout, vdom)**
Firewall Connector to login and logout.
Contains generic methods for working with objects.
This object is useful for working with objects that are not implemented in `FortigateAPI`_

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
host            *str*   Firewall ip address or hostname
username        *str*   Administrator name
password        *str*   Administrator password
scheme          *str*   "https" or "http", by default "https"
port            *int*   TCP port, by default 443 for "https", 80 for "http"
timeout         *int*   Session timeout (minutes), by default 15
vdom            *str*   Name of virtual domain, by default "root"
=============== ======= ============================================================================


login()
.......
**Fortigate.login()** Login to Fortigate


logout()
........
**Fortigate.logout()** Logout Fortigate


delete(url)
...........
**Fortigate.delete(url)** DELETE object from Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


get(url)
........
**Fortigate.get(url)** GET object configured in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
=============== ======= ============================================================================

Return
	*List[dict]* of the objects data


post(url, data)
...............
**Fortigate.post(url, data)** POST (create) object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
data            *dict*  Data of the object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully created or already exists, *<Response [500]>* Object has not been created or already exist in the Fortigate


put(url, data)
..............
**Fortigate.put(url, data)** PUT (update) existing object in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
data            *dict*  Data of the object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


exist(url)
..........
**Fortigate.exist(url)** Check does an object exists in the Fortigate

=============== ======= ============================================================================
Parameter       Type    Description
=============== ======= ============================================================================
url             *str*   REST API URL to the object
=============== ======= ============================================================================

Return
	Session response. *<Response [200]>* Object exist, *<Response [404]>* Object does not exist


Examples - Fortigate
....................

.. code:: python

	from pprint import pprint
	from fortigate_api import Fortigate

	fgt = Fortigate(host="host", username="username", password="password")
	fgt.login()

	# Creates address in the Fortigate
	data = {"name": "ADDRESS",
			"obj-type": "ip",
			"subnet": "127.0.0.100 255.255.255.252",
			"type": "ipmask"}
	response = fgt.post(url="api/v2/cmdb/firewall/address/", data=data)
	print("post", response)  # post <Response [200]>

	# Gets address data from Fortigate
	addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
	addresses = [d for d in addresses if d["name"] == "ADDRESS"]
	pprint(addresses)
	#  [{"comment": "",
	#    "name": "ADDRESS",
	#    "subnet": "127.0.0.100 255.255.255.252",
	#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
	#    ...
	#    }]

	# Update address data in the Fortigate
	data = dict(subnet="127.0.0.255 255.255.255.255")
	response = fgt.put(url="api/v2/cmdb/firewall/address/ADDRESS", data=data)
	print("put", response)  # put <Response [200]>
	addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
	addresses = [d for d in addresses if d["name"] == "ADDRESS"]
	print(addresses[0]["subnet"])  # 127.0.0.255 255.255.255.255

	# Checks for presence of address in the Fortigate
	response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
	print("exist", response)  # <Response [200]>

	# Deletes address from Fortigate
	response = fgt.delete(url="api/v2/cmdb/firewall/address/ADDRESS")
	print("delete", response)  # <Response [200]>

	# Checks for absence of address in the Fortigate
	response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
	print("exist", response)  # <Response [404]>

	fgt.logout()


.. _`./examples/yml/address.yml`: ./examples/yml/address.yml
.. _`./examples/yml/address_group.yml`: ./examples/yml/address_group.yml
.. _`./examples/yml/antivirus.yml`: ./examples/yml/antivirus.yml
.. _`./examples/yml/application.yml`: ./examples/yml/application.yml
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
