"""api/v2/cmdb/firewall/policy.

- Create policy in the Fortigate
- Get all policies from the Fortigate vdom root
- Get filtered policy by policyid (unique identifier)
- Filter policies by name, by operator equals `==`
- Filter policies by operator contains `=@`
- Filter policies by operator not equals `!=`
- Filter policies by multiple conditions
- Update policy data in the Fortigate
- Get all policies with destination address == `192.168.1.2/32`
- Delete policy from the Fortigate by policyid (unique identifier)
- Delete policies from the Fortigate by filter (by name)
- Check for absence of policy in the Fortigate
"""

from pprint import pprint

from fortigate_api import FortiGateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD, logging_error=True)

api.login()  # login is optional

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
response = api.cmdb.firewall.policy.create(data)
print("policy.create", response)  # policy.create <Response [200]>

# Get all policies from the Fortigate vdom root
items = api.cmdb.firewall.policy.get()
print(f"policies count={len(items)}")  # policies count=3

# Get filtered policy by policyid (unique identifier)
items = api.cmdb.firewall.policy.get(policyid=1)
print(f"policies count={len(items)}")  # policies count=1
pprint(items)
#  [{"name": "POLICY",
#    "policyid": 1,
#    "action": "accept",
#    ...
#    }]

# Filter policies by name, by operator equals `==`
items = api.cmdb.firewall.policy.get(filter="name==POLICY")
print(f"policies count={len(items)}")  # policies count=1
policyid = items[0]["policyid"]
print("policyid", policyid)  # policyid 3

# Filter policies by operator contains `=@`
items = api.cmdb.firewall.policy.get(filter="name=@POL")
print(f"policies count={len(items)}")  # policies count=2

# Filter policies by operator not equals `!=`
items = api.cmdb.firewall.policy.get(filter="name!=POLICY")
print(f"policies count={len(items)}")  # policies count=2

# Filter policies by multiple conditions
items = api.cmdb.firewall.policy.get(filter=["name=@POL", "color==6"])
print(f"policies count={len(items)}")  # policies count=0

# Update policy data in the Fortigate
data = dict(policyid=policyid, status="disable")
response = api.cmdb.firewall.policy.update(data=data)
print("policy.update", response)  # policy.update <Response [200]>

# Get all policies with destination address == `192.168.1.2/32`
# Note, the efilter parameter does the same
items = []
addresses = api.cmdb.firewall.address.get(filter="subnet==192.168.1.2 255.255.255.255")
for item in api.cmdb.firewall.policy.get():
    dstaddr = [d["name"] for d in item["dstaddr"]]
    for address in addresses:
        if address["name"] in dstaddr:
            items.append(item)
print(f"policies count={len(items)}")  # policies count=2

# Move policy to top
neighbor = api.cmdb.firewall.policy.get()[0]
response = api.cmdb.firewall.policy.move(policyid, position="before", neighbor=neighbor["policyid"])
print("policy.move", response)  # policy.move <Response [200]>

# Delete policy from the Fortigate by policyid (unique identifier)
response = api.cmdb.firewall.policy.delete(policyid)
print("policy.delete", response)  # policy.delete <Response [200]>

# Delete policies from the Fortigate by filter (by name)
response = api.cmdb.firewall.policy.delete(filter="name==POLICY")
print("policy.delete", response)  # policy.delete <Response [200]>

# Check for absence of policy in the Fortigate
response = api.cmdb.firewall.policy.is_exist(policyid)
print("policy.is_exist", response)  # policy.is_exist False

api.logout()
