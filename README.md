# fortigate-api
Python package to configure Fortigate (Fortios) devices using REST API.


## Installation
```bash
pip install fortigate-api
```

## Known objects
This package implements create/delete/get/update actions with the following objects. 
If you want to manipulate objects not in this list, 
you need to know REST API URL and use [Universal Object](#Universal Object).

    Object Name         GUI and REST API URL to object, FortiOS v6.4
    =================   ======================================================================
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

## Universal Object
    Object Name         REST API URL to object
    =================   ======================================================================
    Object              Process any Fortigate object pointed by REST API URL
                        https://hostname/api/v2/cmdb/...

## Actions for any object
    Action  REST API    Description
    ======  ==========  ==================================================================================
    create  POST        Create new object on Fortigate              param: data
    delete  DELETE      Delete object from Fortigate                param: name
                                                                    param: id (for policy, snmp_community)
    get     GET         Get one or list of objets from Fortigate    params: id, name, filter, filters
    update  PUT         Update existing object on Fortigate         param: data

## Actions for specific objects
    Objects                 Action      Description
    ======================  ==========  ==========================================
    interface, zone         get_all     Get objects in all vdoms
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
    exist(url)                  Check does object exists on Fortigate

## Examples
[Jupiter markdown examples_address](examples_address.ipynb)

### Create firewall connector
firewall connector with mandatory params

```pycon
from fortigate_api import FortigateAPI
fgt = FortigateAPI(host="hostname", username="admin", password="secret")
```

firewall connector with optional params (displayed default values)
```pycon
fgt = FortigateAPI(host="hostname", username="admin", password="secret",
                   port=443, timeout=15, vdom="root")
```

### Get all addresses
```pycon
addresses = fgt.address.get()
```

### Get one address by name
```pycon
address = fgt.address.get(name="172.0.0.100/30")
```

### Get addresses by one param
"==" - name is equal to string
```pycon
addresses = fgt.address.get(filter="name==172.0.0.100/30")
```

### Get addresses by multiple params
"=@" - name contains string
"==" - type is equal to string
```pycon
addresses = fgt.address.get(filters=["name=@172.0.0.", "type==ipmask"])
```

### Create address
```pycon
data = dict(type="ipmask", name="172.0.0.100/30", subnet="172.0.0.100 255.255.255.252")
response = fgt.address.create(data=data)
```

### Update address
```pycon
data = dict(name="172.0.0.100/30", comment="some description")
response = fgt.address.update(data=data)
```

### Delete one address
```pycon
response = fgt.address.delete(name="172.0.0.100/30")
```
