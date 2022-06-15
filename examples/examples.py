"""Examples"""

from pprint import pprint

from fortigate_api import FortigateAPI, Fortigate

fgt = FortigateAPI(host="host", username="username", password="password").login()

print("\n\nExamples - Address\n"
      ".................................................................")

data = {"name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.252",
        "type": "ipmask"}
response = fgt.address.create(data=data)
print("address.create", response)  # address.create <Response [200]>

print("\nGets all addresses from Fortigate")
addresses = fgt.address.get()
print("addresses count", len(addresses))  # addresses count 1727

print("\nGets filtered address by name (unique identifier)")
addresses = fgt.address.get(uid="ADDRESS")
pprint(addresses)
#  [{"comment": "",
#    "name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

print("\nFilters address by operator equals \"==\"")
addresses = fgt.address.get(filter="name==ADDRESS")
print("addresses count", len(addresses))  # addresses count 1

print("\nFilters address by operator contains \"=@\"")
addresses = fgt.address.get(filter="subnet=@127.0")
print("addresses count", len(addresses))  # addresses count 4

print("\nFilters address by operator not equals \"!=\"")
addresses = fgt.address.get(filter="name!=ADDRESS")
print("addresses count", len(addresses))  # addresses count 1726

print("\nFilters address by multiple conditions")
addresses = fgt.address.get(filter=["subnet=@127.0", "type==ipmask"])
print("addresses count", len(addresses))  # addresses count 1

print("\nUpdates address data in the Fortigate")
data = dict(name="ADDRESS", subnet="127.0.0.255 255.255.255.255", color=6)
response = fgt.address.update(uid="ADDRESS", data=data)
print("address.update", response, response.ok)  # address.update <Response [200]> True

print("\nChecks for presence of address in the Fortigate")
response = fgt.address.is_exist(uid="ADDRESS")
print("address.is_exist", response)  # address.is_exist True

print("\nDeletes address from Fortigate by name")
response = fgt.address.delete(uid="ADDRESS")
print("address.delete", response, response.ok)  # address.delete <Response [200]> True

print("\nDeletes addresses from Fortigate by filter (address was deleted before)")
response = fgt.address.delete(filter="name=@ADDRESS")
print("address.delete", response, response.ok)  # address.delete <Response [500]> False

print("\nChecks for absence of address in the Fortigate")
response = fgt.address.is_exist(uid="ADDRESS")
print("address.is_exist", response)  # address.is_exist False

print("\n\nExamples - AddressGroup\n"
      ".................................................................")

print("\nCreates address and address-group in the Fortigate")
data = {"name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.255",
        "type": "ipmask"}
response = fgt.address.create(data=data)
print("address.create", response)  # address.create <Response [200]>
data = {"name": "ADDR_GROUP", "member": [{"name": "ADDRESS"}]}
response = fgt.address_group.create(data=data)
print("address_group.creat", response)  # address_group.creat <Response [200]>

print("\nGets all address-groups from Fortigate")
address_groups = fgt.address_group.get()
print("address_groups count", len(address_groups))  # address_groups count 115

print("\nGets filtered address_group by name (unique identifier)")
address_groups = fgt.address_group.get(uid="ADDR_GROUP")
pprint(address_groups)
#  [{"comment": "",
#    "name": "ADDR_GROUP",
#    "member": [{"name": "ADDRESS", "q_origin_key": "ADDRESS"}],
#    "uuid": "d346aeca-d76a-51ec-7005-541cf3b816f5",
#    ...
#    }]

print("\nFilters address_group by operator equals \"==\"")
address_groups = fgt.address_group.get(filter="name==ADDR_GROUP")
print("address_groups count", len(address_groups))  # address_groups count 1

print("\nFilters address_group by operator contains \"=@\"")
address_groups = fgt.address_group.get(filter="name=@MS")
print("address_groups count", len(address_groups))  # address_groups count 6

print("\nFilters address_group by operator not equals \"!=\"")
address_groups = fgt.address_group.get(filter="name!=ADDR_GROUP")
print("address_groups count", len(address_groups))  # address_groups count 114

print("\nFilters address_group by multiple conditions")
address_groups = fgt.address_group.get(filter=["name=@MS", "color==6"])
print("address_groups count", len(address_groups))  # address_groups count 2

print("\nUpdates address_group data in the Fortigate")
data = dict(name="ADDR_GROUP", color=6)
response = fgt.address_group.update(uid="ADDR_GROUP", data=data)
print("address_group.update", response)  # address_group.update <Response [200]>

print("\nChecks for presence of address_group in the Fortigate")
response = fgt.address_group.is_exist(uid="ADDR_GROUP")
print("address_group.is_exist", response)  # address_group.is_exist True

print("\nDeletes address_group from Fortigate by name")
response = fgt.address_group.delete(uid="ADDR_GROUP")
print("address_group.delete", response)  # address_group.delete <Response [200]>

print("\nDeletes address_groups by filter by filter")
response = fgt.address_group.delete(filter="name=@ADDR_GROUP")
print("address_group.delete", response)  # address_group.delete <Response [200]>

print("\nDeletes address object")
response = fgt.address.delete(uid="ADDRESS")
print("address.delete", response)  # address.delete <Response [200]>

print("\nChecks for absence of address_group in the Fortigate")
response = fgt.address_group.is_exist(uid="ADDR_GROUP")
print("address_group.is_exist", response)  # address_group.is_exist False

print("\n\nExamples - Interface\n"
      ".................................................................")

print("\nGets all interfaces in vdom \"root\" from Fortigate")
interfaces = fgt.interface.get()
print("interfaces count", len(interfaces))  # interfaces count 21

print("\nGets filtered interface by name (unique identifier)")
interfaces = fgt.interface.get(uid="dmz")
pprint(interfaces)
#  [{"name": "dmz",
#    "ip": "0.0.0.0 0.0.0.0",
#    ...
#    }]

print("\nFilters interface by operator equals \"==\"")
interfaces = fgt.interface.get(filter="name==dmz")
print("interfaces count", len(interfaces))  # interfaces count 1

print("\nFilters interface by operator contains \"=@\"")
interfaces = fgt.interface.get(filter="name=@wan")
print("interfaces count", len(interfaces))  # interfaces count 2

print("\nFilters interface by operator not equals \"!=\"")
interfaces = fgt.interface.get(filter="name!=dmz")
print("interfaces count", len(interfaces))  # interfaces count 20

print("\nFilters interface by multiple conditions")
interfaces = fgt.interface.get(filter=["allowaccess=@ping", "detectprotocol==ping"])
print("interfaces count", len(interfaces))  # interfaces count 8

print("\nUpdates interface data in the Fortigate")
data = dict(name="dmz", description="dmz")
response = fgt.interface.update(uid="dmz", data=data)
print("interface.update", response)  # interface.update <Response [200]>

print("\nChecks for presence of interface in the Fortigate")
response = fgt.interface.is_exist(uid="dmz")
print("interface.is_exist", response)  # interface.is_exist True

print("\nChanges virtual domain to \"VDOM\" and gets all interfaces inside this vdom")
fgt.fgt.vdom = "VDOM"
print(f"{fgt!r}")  # Fortigate(host='host', username='username', password='********', vdom='VDOM')
print(fgt.vdom)  # VDOM
interfaces = fgt.interface.get()
print("interfaces count", len(interfaces))  # interfaces count 0

print("\nChanges virtual domain to \"root\"")
fgt.vdom = "root"
print(f"{fgt!r}")  # Fortigate(host='host', username='username', password='********')
print(fgt.vdom)  # root

print("\n\nExamples - Policy\n"
      ".................................................................")

print("\nCreates policy in the Fortigate")
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

print("\nGets all policies from Fortigate")
policies = fgt.policy.get()
print("policies count", len(policies))  # policies count 244

print("\nGets filtered policy by policyid (unique identifier)")
policies = fgt.policy.get(uid="POLICY")
pprint(policies)
#  [{"name": "POLICY",
#    "policyid": 323,
#    "uuid": "521390dc-d771-51ec-9dc2-32467e1bc561",
#    ...
#    }]

print("\nFilters policies by name, by operator equals \"==\"")
policies = fgt.policy.get(filter="name==POLICY")
print("policies count", len(policies))  # policies count 1
policyid = policies[0]["policyid"]
print("policyid", policyid)  # policyid 323

print("\nFilters policies by operator contains \"=@\"")
policies = fgt.policy.get(filter="name=@POL")
print("policies count", len(policies))  # policies count 6

print("\nFilters policies by operator not equals \"!=\"")
policies = fgt.policy.get(filter="name!=POLICY")
print("policies count", len(policies))  # policies count 243

print("\nFilters policies by multiple conditions")
policies = fgt.policy.get(filter=["name=@POL", "color==6"])
print("policies count", len(policies))  # policies count 2

print("\nUpdates policy data in the Fortigate")
data = dict(policyid=policyid, status="disable")
response = fgt.policy.update(uid="POLICY", data=data)
print("policy.update", response)  # policy.update <Response [200]>

print("\nChecks for presence of policy in the Fortigate")
response = fgt.policy.is_exist(uid=policyid)
print("policy.is_exist", response)  # policy.is_exist True

print("\nGets all policies with destination address == \"192.168.1.2/32\"")
policies = []
addresses = fgt.address.get(filter="subnet==192.168.1.2 255.255.255.255")
for policy in fgt.policy.get():
    dstaddr = [d["name"] for d in policy["dstaddr"]]
    for address in addresses:
        if address["name"] in dstaddr:
            policies.append(policy)
print("policies count", len(policies))  # policies count 2

print("\nMoves policy to top")
neighbor = fgt.policy.get()[0]
response = fgt.policy.move(uid=policyid, position="before", neighbor=neighbor["policyid"])
print("policy.move", response, response.ok)  # policy.move <Response [200]> False

print("\nDeletes policy from Fortigate by policyid (unique identifier)")
response = fgt.policy.delete(uid=policyid)
print("policy.delete", response, response.ok)  # policy.delete <Response [200]> True

print("\nDeletes policies from Fortigate by filter (by name)")
response = fgt.policy.delete(filter="name==POLICY")
print("policy.delete", response, response.ok)  # policy.delete <Response [200]> True

print("\nChecks for absence of policy in the Fortigate")
response = fgt.policy.is_exist(uid=policyid)
print("policy.is_exist", response)  # policy.is_exist False

print("\n\nExamples - Policy extended filter\n"
      ".................................................................")

print("\nCreates address and address_groupin the Fortigate")
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

print("\nCreates policy in the Fortigate")
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

print("\nGets the rules where source prefix is equals 127.0.1.0/30")
efilter = "srcaddr==127.0.1.0/30"
policies = fgt.policy.get(efilter=efilter)
print(f"{efilter=}", len(policies))  # efilter='srcaddr==127.0.1.0/30' 1

print("\nGets the rules where source prefix is not equals 127.0.1.0/30")
efilter = "srcaddr!=127.0.1.0/30"
policies = fgt.policy.get(efilter=efilter)
print(f"{efilter=}", len(policies))  # efilter='srcaddr!=127.0.1.0/30' 35

print("\nGets the rules where source addresses are in subnets of 127.0.1.0/24")
efilter = "srcaddr<=127.0.1.0/24"
policies = fgt.policy.get(efilter=efilter)
print(f"{efilter=}", len(policies))  # efilter='srcaddr<=127.0.1.0/24' 1

print("\nGets the rules where source prefixes are supernets of address 127.0.1.1/32")
efilter = "srcaddr>=127.0.1.1/32"
policies = fgt.policy.get(efilter=efilter)
print(f"{efilter=}", len(policies))  # efilter='srcaddr>=127.0.1.1/32' 7

print("\nGets the rules where source prefix are equals 127.0.1.0/30 and")
print("\ndestination prefix are equals 127.0.2.0/30")
efilters = ["srcaddr==127.0.1.0/30", "dstaddr==127.0.2.0/30"]
policies = fgt.policy.get(efilter=efilters)
print(f"{efilters=}", len(policies))
print("\nefilters=['srcaddr==127.0.1.0/30', 'dstaddr==127.0.2.0/30'] 1")

print("\nDelete policy, address-group, addresses from Fortigate (order is important)")
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

print("\n\nExamples - Fortigate\n"
      ".................................................................")

fgt = Fortigate(host="host", username="username", password="password").login()

# Creates address in the Fortigate
data = {"name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.252",
        "type": "ipmask"}
response = fgt.post(url="api/v2/cmdb/firewall/address/", data=data)
print("post", response)  # post <Response [200]>

print("\nGets address data from Fortigate")
addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
addresses = [d for d in addresses if d["name"] == "ADDRESS"]
pprint(addresses)
#  [{"comment": "",
#    "name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

print("\nUpdate address data in the Fortigate")
data = dict(subnet="127.0.0.255 255.255.255.255")
response = fgt.put(url="api/v2/cmdb/firewall/address/ADDRESS", data=data)
print("put", response)  # put <Response [200]>
addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
addresses = [d for d in addresses if d["name"] == "ADDRESS"]
print(addresses[0]["subnet"])  # 127.0.0.255 255.255.255.255

print("\nChecks for presence of address in the Fortigate")
response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
print("exist", response)  # <Response [200]>

print("\nDeletes address from Fortigate")
response = fgt.delete(url="api/v2/cmdb/firewall/address/ADDRESS")
print("delete", response)  # <Response [200]>

print("\nChecks for absence of address in the Fortigate")
response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
print("exist", response)  # <Response [404]>

fgt.logout()

print("\n\nExamples - HTTP\n"
      ".................................................................")
fgt = Fortigate(host="host", username="username", password="password").login()
