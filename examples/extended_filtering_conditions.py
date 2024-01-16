"""Extended Filter conditions api/v2/cmdb/firewall/policy.

- Create address, address-group and policy in the Fortigate
- Get the rules where source prefix is equals 127.0.0.0/30
- Get the rules where source prefix is not equals 127.0.0.0/30
- Get the rules where source addresses are in subnets of 127.0.0.0/24
- Get the rules where source prefixes are supernets of address 127.0.0.1/32
- Get the rules where source are equals 127.0.0.0/30 and destination are equals 127.0.2.0/30
- Delete policy, address-group, addresses from the Fortigate (order is important)
"""

import logging

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Create address, address-group and policy in the Fortigate
for idx in range(2):
    data = {
        "name": f"ADDRESS_{idx}",
        "obj-type": "ip",
        "subnet": f"127.0.{idx}.0 255.255.255.252",
        "type": "ipmask",
    }
    response = api.cmdb.firewall.address.create(data=data)
    print("address.create", response)  # address.create <Response [200]>
data = {"name": "ADDR_GROUP", "member": [{"name": "ADDRESS_1"}]}
response = api.cmdb.firewall.addrgrp.create(data=data)
print("addrgrp.create", response)  # addrgrp.create <Response [200]>
data = dict(
    name="POLICY",
    status="enable",
    action="accept",
    srcintf=[{"name": "any"}],
    dstintf=[{"name": "any"}],
    srcaddr=[{"name": "ADDRESS_0"}],
    dstaddr=[{"name": "ADDR_GROUP"}],
    service=[{"name": "ALL"}],
    schedule="always",
)
response = api.cmdb.firewall.policy.create(data=data)
print("policy.create", response)  # policy.create <Response [200]>

# Get the rules where source prefix is equals 127.0.0.0/30
efilter = "srcaddr==127.0.0.0/30"
items = api.cmdb.firewall.policy.get(efilter=efilter)
print(f"{efilter=}", len(items))  # efilter="srcaddr==127.0.0.0/30" 1

# Get the rules where source prefix is not equals 127.0.0.0/30
efilter = "srcaddr!=127.0.0.0/30"
items = api.cmdb.firewall.policy.get(efilter=efilter)
print(f"{efilter=}", len(items))  # efilter="srcaddr!=127.0.0.0/30" 3

# Get the rules where source addresses are in subnets of 127.0.0.0/24
efilter = "srcaddr<=127.0.0.0/24"
items = api.cmdb.firewall.policy.get(efilter=efilter)
print(f"{efilter=}", len(items))  # efilter="srcaddr<=127.0.0.0/24" 1

# Get the rules where source prefixes are supernets of address 127.0.0.1/32
efilter = "srcaddr>=127.0.0.1/32"
items = api.cmdb.firewall.policy.get(efilter=efilter)
print(f"{efilter=}", len(items))  # efilter="srcaddr>=127.0.0.1/32" 3

# Get the rules where source are equals 127.0.0.0/30 and destination are equals 127.0.2.0/30
efilter = ["srcaddr==127.0.0.0/30", "dstaddr==127.0.1.0/30"]
items = api.cmdb.firewall.policy.get(efilter=efilter)
print(f"{efilter=}", len(items))
# efilter=["srcaddr==127.0.0.0/30", "dstaddr==127.0.1.0/30"] 1

# Delete policy, address-group, addresses from the Fortigate (order is important)
response = api.cmdb.firewall.policy.delete(filter="name==POLICY")
print("policy.delete", response)  # policy.delete <Response [200]>
response = api.cmdb.firewall.addrgrp.delete("ADDR_GROUP")
print("addrgrp.delete", response)  # addrgrp.delete <Response [200]>
response = api.cmdb.firewall.address.delete("ADDRESS_0")
print("address.delete", response)  # address.delete <Response [200]>
response = api.cmdb.firewall.address.delete("ADDRESS_1")
print("address.delete", response)  # address.delete <Response [200]>

api.logout()
