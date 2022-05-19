fortigate-api
=============

Python package for configuring Fortigate (Fortios) devices using REST API.
With this package, you can create, delete, get, update any objects in the Fortigate.
The most commonly used objects are implemented in the *FortigateAPI* methods, but you can manipulate
any other objects that can be accessed through the API using the *Fortigate* methods.

.. contents::

.. sectnum::


Installation
------------

Install the package by running

.. code:: bash

    pip install fortigate-api

or

.. code:: bash

    pip install git+https://github.com/vladimirs-git/fortigate-api


FortigateAPI(host, username, password, port, timeout, vdom)
-----------------------------------------------------------
**FortigateAPI** - a set of methods for working with the most commonly used objects

=================== ================================================================================
Supported objects   GUI and REST API URL to the object, FortiOS v6.4
=================== ================================================================================
Address             https://hostname/ng/firewall/address
					https://hostname/api/v2/cmdb/firewall/address/
AddressGroup        https://hostname/ng/firewall/address
					https://hostname/api/v2/cmdb/firewall/addrgrp/
Antivirus           https://hostname/ng/utm/antivirus/profile
					https://hostname/api/v2/cmdb/antivirus/profile/
Application         https://hostname/ng/utm/appctrl/sensor
					https://hostname/api/v2/cmdb/application/list/
Interface           https://hostnae/ng/interface
					https://hostname/api/v2/cmdb/system/interface/
InternetService     https://hostnae/ng/firewall/internet_service
					https://hostname/api/v2/cmdb/firewall/internet-service/
IpPool              https://hostname/ng/firewall/ip-pool
					https://hostname/api/v2/cmdb/firewall/ippool/
Policy              https://hostname/ng/firewall/policy/policy/standard
					https://hostname/api/v2/cmdb/firewall/policy/
Schedule            https://hostname/ng/firewall/schedule
					https://hostname/api/v2/cmdb/firewall.schedule/onetime/
Service             https://hostname/ng/firewall/service
					https://hostname/api/v2/cmdb/firewall.service/custom/
ServiceCategory     https://hostname/ng/firewall/service
					https://hostname/api/v2/cmdb/firewall.service/category/
ServiceGroup        https://hostname/ng/firewall/service
					https://hostname/api/v2/cmdb/firewall.service/group/
SnmpCommunity       https://hostname/ng/system/snmp
					https://hostname/api/v2/cmdb/system.snmp/community/
VirtualIp           https://hostname/ng/firewall/virtual-ip
					https://hostname/api/v2/cmdb/firewall/vip/
Zone                https://hostnae/ng/interface
					https://hostname/api/v2/cmdb/system/zone/

=================== ================================================================================


=============== ======= ================================================================================================
Parameter        Type    Description
=============== ======= ================================================================================================
host            *str*   Firewall ip address or hostname
username        *str*   Administrator name
password        *str*   Administrator password
port            *int*   HTTPS port, by default 443
timeout         *int*   Session timeout (minutes), by default 15
vdom            *str*   Name of virtual domain, by default "root"
=============== ======= ================================================================================================


Address
-------


address.create(data)
....................
**fgt.address.create(data)** - Creates address-object in the Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
data            *dict*  Data of the address-object
=============== ======= ================================================================================================

Return
	Session response. *<Response [200]>* Object successfully created, *<Response [500]>* Object already exist in the Fortigate


address.delete(name)
....................
**fgt.address.delete(name)** - Deletes address-object from Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
name            *str*   Name of the address-object
=============== ======= ================================================================================================

Return
	Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


address.get(name, filter)
.........................
**fgt.address.get(name, filter)** - Gets address-objects, all or filtered by some of params. Need to use only one of params.

=============== =================== ====================================================================================
Parameter       Type                Description
=============== =================== ====================================================================================
name            *str*       	    Filters address-object by name
filter          *str*, *List[str]*  Filters address-objects by one *str* or by multiple *List[str]* conditions: equal "==", not equal "!=", contain "=@"
=============== =================== ====================================================================================

Return
	*List[dict]* List of address-objects


address.update(data)
....................
**fgt.address.update(data)** - Updates address-object in the Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
data            *dict*  Data of the address-object
=============== ======= ================================================================================================

Return
	Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


address.is_exist(name)
......................
**fgt.address.is_exist(name)** - Checks does an address-object exists in the Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
name            *str*   Name of the address-object
=============== ======= ================================================================================================

Return
	*bool* True - object exist, False - object does not exist


Examples
........
- Creates address in the Fortigate
- Gets all addresses from Fortigate
- Gets filtered address by name (unique identifier)
- Filters address by operator equal "=="
- Filters address by operator contains "=@"
- Filters address by operator not equal "!="
- Updates address data in the Fortigate
- Checks for presence of address in the Fortigate
- Deletes address from Fortigate
- Checks for absence of address in the Fortigate

.. code:: python

	from pprint import pprint
	from fortigate_api import FortigateAPI

	fgt = FortigateAPI(host="host", username="username", password="password")
	fgt.login()

	# Creates address in the Fortigate
	data = {"name": "127.0.0.100",
			"obj-type": "ip",
			"subnet": "127.0.0.100 255.255.255.252",
			"type": "ipmask"}
	response = fgt.address.create(data=data)
	print("post", response)  # post <Response [200]>

	# Gets all addresses from Fortigate
	addresses = fgt.address.get()
	print("addresses count", len(addresses))  # addresses count 1727

	# Gets filtered address by name (unique identifier)
	addresses = fgt.address.get(name="127.0.0.100")
	pprint(addresses)
	#  [{"comment": "",
	#    "name": "127.0.0.100",
	#    "subnet": "127.0.0.100 255.255.255.252",
	#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
	#    ...
	#    }]

	# Filters address by operator equal "=="
	addresses = fgt.address.get(filter="name==127.0.0.100")
	print("addresses count", len(addresses))  # addresses count 1

	# Filters address by operator contains "=@"
	addresses = fgt.address.get(filter="subnet=@127.0")
	print("addresses count", len(addresses))  # addresses count 4

	# Filters address by operator not equal "!="
	addresses = fgt.address.get(filter="name!=127.0.0.100")
	print("addresses count", len(addresses))  # addresses count 1726

	# Filters address by multiple conditions
	addresses = fgt.address.get(filter=["subnet=@127.0", "type==ipmask"])
	print("addresses count", len(addresses))  # addresses count 1

	# Updates address data in the Fortigate
	data = dict(name="127.0.0.100", subnet="127.0.0.255 255.255.255.255", color=6)
	response = fgt.address.update(data=data)
	print("put", response)  # put <Response [200]>

	# Checks for presence of address in the Fortigate
	response = fgt.address.is_exist(name="127.0.0.100")
	print("is_exist", response)  # is_exist True

	# Deletes address from Fortigate
	response = fgt.address.delete(name="127.0.0.100")
	print("delete", response)  # delete <Response [200]>

	# Checks for absence of address in the Fortigate
	response = fgt.address.is_exist(name="127.0.0.100")
	print("is_exist", response)  # is_exist False

	fgt.logout()



AddressGroup
-------


address_group.create(data)
....................
**fgt.address_group.create(data)** - Creates address-group-object in the Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
data            *dict*  Data of the address-group-object
=============== ======= ================================================================================================

Return
	Session response. *<Response [200]>* Object successfully created, *<Response [500]>* Object already exist in the Fortigate


address_group.delete(name)
....................
**fgt.address_group.delete(name)** - Deletes address-group-object from Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
name            *str*   Name of the address-group-object
=============== ======= ================================================================================================

Return
	Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate


address_group.get(name, filter)
.........................
**fgt.address_group.get(name, filter)** - Gets address-group-objects, all or filtered by some of params. Need to use only one of params.

=============== =================== ====================================================================================
Parameter       Type                Description
=============== =================== ====================================================================================
name            *str*       	    Filters address-group-object by name
filter          *str*, *List[str]*  Filters address-group-objects by one *str* or by multiple *List[str]* conditions: equal "==", not equal "!=", contain "=@"
=============== =================== ====================================================================================

Return
	*List[dict]* List of address-group-objects


address_group.update(data)
....................
**fgt.address_group.update(data)** - Updates address-group-object in the Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
data            *dict*  Data of the address-group-object
=============== ======= ================================================================================================

Return
	Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated


address_group.is_exist(name)
......................
**fgt.address_group.is_exist(name)** - Checks does an address-group-object exists in the Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
name            *str*   Name of the address-group-object
=============== ======= ================================================================================================

Return
	*bool* True - object exist, False - object does not exist


Examples
........
- Creates address-group in the Fortigate
- Gets all address-groups from Fortigate
- Gets filtered address-group by name (unique identifier)
- Filters address-group by operator equal "=="
- Filters address-group by operator contains "=@"
- Filters address-group by operator not equal "!="
- Updates address-group data in the Fortigate
- Checks for presence of address-group in the Fortigate
- Deletes address-group from Fortigate
- Checks for absence of address-group in the Fortigate

.. code:: python

	from pprint import pprint
	from fortigate_api import FortigateAPI

	fgt = FortigateAPI(host="host", username="username", password="password")
	fgt.login()

	# Creates address and address-group in the Fortigate
	data = {"name": "127.0.0.100",
			"obj-type": "ip",
			"subnet": "127.0.0.100 255.255.255.255",
			"type": "ipmask"}
	response = fgt.address.create(data=data)
	print("post", response)  # post <Response [200]>

	data = {"name": "ADDR_GROUP", "member": [{"name": "127.0.0.100"}]}
	response = fgt.address_group.create(data=data)
	print("post", response)  # post <Response [200]>

	# Gets all address-groups from Fortigate
	address_groups = fgt.address_group.get()
	print("address_groups count", len(address_groups))  # address_groups count 115

	# Gets filtered address by name (unique identifier)
	address_groups = fgt.address_group.get(name="ADDR_GROUP")
	pprint(address_groups)
	#  [{"comment": "",
	#    "name": "ADDR_GROUP",
	#    "member": [{"name": "127.0.0.100", "q_origin_key": "127.0.0.100"}],
	#    "uuid": "d346aeca-d76a-51ec-7005-541cf3b816f5",
	#    ...
	#    }]

	# Filters address by operator equal "=="
	address_groups = fgt.address_group.get(filter="name==ADDR_GROUP")
	print("address_groups count", len(address_groups))  # address_groups count 1

	# Filters address by operator contains "=@"
	address_groups = fgt.address_group.get(filter="name=@MS")
	print("address_groups count", len(address_groups))  # address_groups count 6

	# Filters address by operator not equal "!="
	address_groups = fgt.address_group.get(filter="name!=ADDR_GROUP")
	print("address_groups count", len(address_groups))  # address_groups count 114

	# Filters address by multiple conditions
	address_groups = fgt.address_group.get(filter=["name=@MS", "color==6"])
	print("address_groups count", len(address_groups))  # address_groups count 2

	# Updates address data in the Fortigate
	data = dict(name="ADDR_GROUP", color=6)
	response = fgt.address_group.update(data=data)
	print("put", response)  # put <Response [200]>

	# Checks for presence of address in the Fortigate
	response = fgt.address_group.is_exist(name="ADDR_GROUP")
	print("is_exist", response)  # is_exist True

	# Deletes address from Fortigate
	response = fgt.address_group.delete(name="ADDR_GROUP")
	print("delete", response)  # delete <Response [200]>

	# Checks for absence of address in the Fortigate
	response = fgt.address_group.is_exist(name="ADDR_GROUP")
	print("is_exist", response)  # is_exist False

	fgt.logout()



Policy
------


policy.create(data)
...................
**fgt.policy.create(data)** - Creates policy-object in the Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
data            *dict*  Data of the policy-object
=============== ======= ================================================================================================

Return
	Session response. *<Response [200]>* Object successfully created, *<Response [500]>* Object already exist in the Fortigate


policy.delete(name)
...................
**fgt.policy.delete(name)** - Deletes policy-object from Fortigate

=============== =============== ========================================================================================
Parameter       Type            Description
=============== =============== ========================================================================================
id              *str*, *int*    Identifier of the policy-object
=============== =============== ========================================================================================

Return
	Session response. *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate

policy.delete_name(name)
........................
**fgt.policy.delete(name)** - Deletes policy-objects with the same name from Fortigate

=============== =============== ========================================================================================
Parameter       Type            Description
=============== =============== ========================================================================================
name            *str*           Name of the policy-objects
=============== =============== ========================================================================================

Return
	Session response. *List[Response]* - where *<Response [200]>* Object successfully deleted, *<Response [404]>* Object absent in the Fortigate

policy.get(id, name, filter)
............................
**fgt.policy.get(id, name, filter)** - Gets policy-objects, all or filtered by some of params. Need to use only one of params.

=============== =================== ====================================================================================
Parameter       Type                Description
=============== =================== ====================================================================================
id              *str*, *int*        Filters policy-object by identifier
name            *str*       	    Filters policy-object by name
filter          *str*, *List[str]*  Filters policy-objects by one *str* or by multiple *List[str]* conditions: equal "==", not equal "!=", contain "=@"
=============== =================== ====================================================================================

Return
	*List[dict]* List of policy-objects

policy.is_exist(name)
.....................
**fgt.policy.is_exist(name)** - Checks does an policy-object exists in the Fortigate

=============== =================== ====================================================================================
Parameter       Type                Description
=============== =================== ====================================================================================
id              *str*, *int*        Identifier of the policy-object
=============== =================== ====================================================================================

Return
	*bool* True - object exist, False - object does not exist

policy.move(id, position, neighbor)
...................................
**fgt.policy.move(id, position, neighbor)** - Move policy to before/after other neighbor-policy

=============== =================== ====================================================================================
Parameter       Type                Description
=============== =================== ====================================================================================
id              *str*, *int*        Identifier of policy being moved
position        *str*               "before" or "after" neighbor
neighbor        *str*, *int*        Policy will be moved near to this neighbor-policy
=============== =================== ====================================================================================

Return
	Session response. *<Response [200]>* Policy successfully moved, *<Response [500]>* Policy has not been moved

policy.update(data)
...................
**fgt.policy.update(data)** - Updates policy-object in the Fortigate

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
data            *dict*  Data of the policy-object
=============== ======= ================================================================================================

Return
	Session response. *<Response [200]>* Object successfully updated, *<Response [404]>* Object has not been updated

Examples
........
- Creates policy in the Fortigate
- Gets all policies from Fortigate
- Gets filtered policy by id (unique identifier)
- Filters policies by operator equal "=="
- Filters policies by operator contains "=@"
- Filters policies by operator not equal "!="
- Updates policy data in the Fortigate
- Checks for presence of policy in the Fortigate
- Gets all policies with destination address == "192.168.1.2/32"
- Deletes policy from Fortigate
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
	print("post", response)  # post <Response [200]>

	# Gets all policies from Fortigate
	policies = fgt.policy.get()
	print("policies count", len(policies))  # policies count 244

	# Gets filtered policy by id (unique identifier)
	policies = fgt.policy.get(name="POLICY")
	pprint(policies)
	#  [{"name": "POLICY",
	#    "policyid": 323,
	#    "uuid": "521390dc-d771-51ec-9dc2-32467e1bc561",
	#    ...
	#    }]

	# Filters policies by operator equal "=="
	policies = fgt.policy.get(filter="name==POLICY")
	print("policies count", len(policies))  # policies count 1
	policyid = policies[0]["policyid"]
	print(policyid)  # 323

	# Filters policies by operator contains "=@"
	policies = fgt.policy.get(filter="name=@POL")
	print("policies count", len(policies))  # policies count 6

	# Filters policies by operator not equal "!="
	policies = fgt.policy.get(filter="name!=POLICY")
	print("policies count", len(policies))  # policies count 243

	# Filters policies by multiple conditions
	policies = fgt.policy.get(filter=["name=@POL", "color==6"])
	print("policies count", len(policies))  # policies count 2

	# Updates policy data in the Fortigate
	data = dict(policyid=policyid, status="disable")
	response = fgt.policy.update(data=data)
	print("put", response)  # put <Response [200]>

	# Checks for presence of policy in the Fortigate
	response = fgt.policy.is_exist(id=policyid)
	print("is_exist", response)  # is_exist True

	# Gets all policies with destination address == "192.168.1.2/32"
	policies = []
	addresses = fgt.address.get(filter="subnet==192.168.1.2 255.255.255.255")
	for policy in fgt.policy.get():
		dstaddr = [d["name"] for d in policy["dstaddr"]]
		for address in addresses:
			if address["name"] in dstaddr:
				policies.append(policy)
	pprint(policies)
	print("policies count", len(policies))  # policies count 2

	# Moves policy to top
	neighbor = fgt.policy.get()[0]
	response = fgt.policy.move(id=policyid, position="before", neighbor=neighbor["policyid"])
	print("move", response)  # move <Response [200]>

	# Deletes policy from Fortigate
	response = fgt.policy.delete(id=policyid)
	print("delete", response)  # delete <Response [200]>

	# Checks for absence of policy in the Fortigate
	response = fgt.policy.is_exist(id=policyid)
	print("is_exist", response)  # is_exist False

	fgt.logout()


Fortigate(host, username, password, port, timeout, vdom)
--------------------------------------------------------
**Fortigate** - Firewall Connector to login and logout.
Calls generic methods for working with objects: delete, get, post, put, exist.
This object is useful for working with firewall objects that are not implemented in the *FortigateAPI*.

=============== ======= ================================================================================================
Parameter       Type    Description
=============== ======= ================================================================================================
host            *str*   Firewall ip address or hostname
username        *str*   Administrator name
password        *str*   Administrator password
port            *int*   HTTPS port, by default 443
timeout         *int*   Session timeout (minutes), by default 15
vdom            *str*   Name of virtual domain, by default "root"
=============== ======= ================================================================================================


=========================== ============================================================================================
Method                      Description
=========================== ============================================================================================
Fortigate.login()           Login to Fortigate
Fortigate.logout()          Logout Fortigate
Fortigate.delete(url)       DELETE object from Fortigate. Returns session response.
Fortigate.get(url)          GET object configured in the Fortigate. Returns session response.
Fortigate.post(url, data)   POST (create) object in the Fortigate based in data. Returns session response.
Fortigate.put(url, data)    PUT (update) existing object in the Fortigate. Returns session response.
Fortigate.exist(url)        Check does an object exists in the Fortigate. Returns session response.
=========================== ============================================================================================


Examples
........

.. code:: python

	from pprint import pprint
	from fortigate_api import Fortigate

	fgt = Fortigate(host="host", username="username", password="password")
	fgt.login()

	# Creates address in the Fortigate
	data = {"name": "127.0.0.100",
			"obj-type": "ip",
			"subnet": "127.0.0.100 255.255.255.252",
			"type": "ipmask"}
	response = fgt.post(url="api/v2/cmdb/firewall/address/", data=data)
	print("post", response)
	# post <Response [200]>

	# Gets address data from Fortigate
	addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
	addresses = [d for d in addresses if d["name"] == "127.0.0.100"]
	pprint(addresses)
	#  [{"comment": "",
	#    "name": "127.0.0.100",
	#    "subnet": "127.0.0.100 255.255.255.252",
	#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
	#    ...
	#    }]

	# Update address data in the Fortigate
	data = dict(subnet="127.0.0.255 255.255.255.255")
	response = fgt.put(url="api/v2/cmdb/firewall/address/127.0.0.100", data=data)
	print("put", response)
	# put <Response [200]>
	addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
	addresses = [d for d in addresses if d["name"] == "127.0.0.100"]
	print(addresses[0]["subnet"])
	# 127.0.0.255 255.255.255.255

	# Checks for presence of address in the Fortigate
	response = fgt.exist(url="api/v2/cmdb/firewall/address/127.0.0.100")
	print("exist", response)
	# <Response [200]>

	# Deletes address from Fortigate
	response = fgt.delete(url="api/v2/cmdb/firewall/address/127.0.0.100")
	print("delete", response)
	# <Response [200]>

	# Checks for absence of address in the Fortigate
	response = fgt.exist(url="api/v2/cmdb/firewall/address/127.0.0.100")
	print("exist", response)
	# <Response [404]>

	fgt.logout()
