# fortigate-api

Python package to configure Fortigate (Fortios) devices using REST API. With this package, you can
create, delete, get, update the any objects in the firewall. The most commonly used objects
implemented in the methods of this package, but you can manipulate any other objects that you can
access via the API.

## Installation

```bash
pip install fortigate-api
```

## Object

    Object Name         GUI and REST API URL to the object, FortiOS v6.4
    =================   ======================================================================
    Object              Process any Fortigate object pointed by REST API URL
                        https://hostname/api/v2/cmdb/...

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

## Methods for any object

All above listed objects have methods: create, delete, get, update. Params for objets _policy_ and _
snmp_community_ are different from the others (id instead of name). More details in method
docstrings (in code).

    Method  REST API    Description                     Params
    ======  ==========  ==============================  ============================================
    create  POST        Create new object on Fortigate  param: data
    delete  DELETE      Delete object from Fortigate    param: name
                                                        param for policy: policyid
                                                        param for snmp_community: id 
    get     GET         Get objets from Fortigate       params: name, filter, filters
                                                        params for policy: policyid, filter, filters 
                                                        params for snmp_community: id, filter, filters
    update  PUT         Update object on Fortigate      param: data

## Methods for specific objects

Some objects have specific methods. For example method _move_ is implemented only for object policy.
Policy can be moved up/down and change order in configured policies list. More details in method
docstrings (in code).

    Objects                 Action      Description
    ======================  ==========  ==========================================
    interface, zone         get_all     Get objects from all vdoms
    policy, snmp_community  delete_name Delete multiple objects with the same name
    policy                  move        Move policy to before/after other policy

## Fortigate methods

    Method Name                 Description
    ==========================  ===============================================
    login()                     Login to Fortigate
    logout()                    Logout Fortigate
    delete(url)                 DELETE object from Fortigate
    get(url)                    GET object configured on Fortigate
    post(url, data)             POST (create) object on Fortigate based on data
    put(url, data)              PUT (update) existing object on Fortigate
    exist(url)                  Check does an object exists on Fortigate

## Examples

Jupiter markdown example [examples_address.ipynb](examples/examples_address.ipynb)

### Firewall API connector

    param       Required/Optional   Defaul  Description
    ==========  ==================  ======  ===========
    host        mandatory                   Firewall ip address or hostname
    username    mandatory                   Administrator name
    password    mandatory                   Administrator password
    port        optional            443     HTTPS port to REST API interface
    timeout     optional            15      Ssession timeout (minutes)
    vdom        optional            root    Name of virtual domain

Firewall connector with minimum required params

```pycon
from fortigate_api import FortigateAPI
fgt = FortigateAPI(host="hostname", username="admin", password="secret")
```

Firewall connector with optional params

```pycon
fgt = FortigateAPI(host="hostname", username="admin", password="secret",
                   port=1443, timeout=60, vdom="name")
```

### Configuring Address objects on Fortigate

Unique identifier for address object is _name_. Pointing address by _name_ you will get only one
object. Address data example for FortiOS v6.4 [examples/address.yml](examples/address.yml)

#### Get all addresses

```pycon
addresses = fgt.address_groups.get()
```

#### Get address by name

```pycon
address = fgt.address_groups.get(name="127.0.0.100_30")
```

#### Get addresses by one param

Get all addresses with type _ipmask_. Filters:
"==" - type is equal to _ipmask_.

```pycon
addresses = fgt.address_groups.get(filter="type==ipmask")
```

#### Get addresses by multiple params

Get all addresses where type is _fqdn_ and comment field contains _description_. Filters:
"==" - type is equal to _fqdn_,
"=@" - comment field contains _description_ string.

```pycon
addresses = fgt.address_groups.get(filters=["type==fqdn", "comment=@description", ])
```

#### Create address

```pycon
data = dict(type="ipmask", name="127.0.0.100_30", subnet="127.0.0.100 255.255.255.252")
response = fgt.address_groups.create(data=data)
```

#### Update address

```pycon
data = dict(name="127.0.0.100_30", comment="description")
response = fgt.address_groups.update(data=data)
```

#### Delete address

```pycon
response = fgt.address_groups.delete(name="127.0.0.100_30")
```

### Configuring Policy objects on Fortigate

Unique identifier for policy object is _id_. Pointing policy by _id_ you will get only one object.
Pointing policy by _name_ you can get multiple objects. Policy data example for FortiOS
v6.4 [examples/policy.yml](examples/policy.yml)

#### Get all policies

```pycon
policies = fgt.policy.get()
```

#### Get policy by id

Pointing policy by _policyid_ you will get only one object.

```pycon
policy = fgt.policy.get(policyid=1)
```

#### Get policies by name

Pointing policy by _name_ you can get multiple object.

```pycon
policy = fgt.policy.get(name="policy1")
```

#### Get policies by one param

Get all policies with status _enable_. Filters: "==" - status is equal to _fqdn_.

```pycon
policies = fgt.policy.get(filter="status==enable")
```

#### Get policies by multiple params

Get all policies where status is _disable_ and comments field contains _description_. Filters:
"==" - status is equal to _disable_,
"=@" - comments field contains _description_ string.

```pycon
policies = fgt.policy.get(filters=["status==disable", "comments=@description"])
```

#### Create policy

```pycon
data = dict(name="policy1", srcaddr="127.0.0.100_30", dstaddr="127.0.0.104_30")
response = fgt.policy.create(data=data)
```

#### Update policy

```pycon
data = dict(policyid=1, comment="description")
response = fgt.policy.update(data=data)
```

#### Delete policy by id

```pycon
response = fgt.policy.delete(id=1)
```

#### Delete all policies with name

```pycon
response = fgt.policy.delete(name="policy1")
```

#### Move policy to before/after other neighbor-policy

```pycon
response = fgt.policy.move(id=1, position="after", neighbor=2)
```
