"""Policy examples.

- Create policy in the Fortigate
- Get all policies from the Fortigate
- Get filtered policy by policyid (unique identifier)
- Filter policies by name, by operator *equals* "=="
- Filter policies by operator *contains* "=@"
- Filter policies by operator *not equals* "!="
- Update policy data in the Fortigate
- Check for presence of policy in the Fortigate
- Get all policies with destination address == "192.168.1.2/32"
- Delete policy from the Fortigate by policyid (unique identifier)
- Delete policies from the Fortigate by filter (by name)
- Check for absence of policy in the Fortigate
"""

from pprint import pprint

from fortigate_api import FortigateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
fgt.login()

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

print("\nGets all policies from the Fortigate")
policies = fgt.policy.get()
print(f"policies count={len(policies)}")  # policies count=244

print("\nGets filtered policy by policyid (unique identifier)")
policies = fgt.policy.get(uid=1)
pprint(policies)
#  [{"name": "POLICY",
#    "policyid": 1,
#    "action": "accept",
#    ...
#    }]

print("\nFilters policies by name, by operator equals \"==\"")
policies = fgt.policy.get(filter="name==POLICY")
print(f"policies count={len(policies)}")  # policies count=1
policyid = policies[0]["policyid"]
print("policyid", policyid)  # policyid 323

print("\nFilters policies by operator contains \"=@\"")
policies = fgt.policy.get(filter="name=@POL")
print(f"policies count={len(policies)}")  # policies count=6

print("\nFilters policies by operator not equals \"!=\"")
policies = fgt.policy.get(filter="name!=POLICY")
print(f"policies count={len(policies)}")  # policies count=243

print("\nFilters policies by multiple conditions")
policies = fgt.policy.get(filter=["name=@POL", "color==6"])
print(f"policies count={len(policies)}")  # policies count=2

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
print(f"policies count={len(policies)}")  # policies count=2

print("\nMoves policy to top")
neighbor = fgt.policy.get()[0]
response = fgt.policy.move(uid=policyid, position="before", neighbor=neighbor["policyid"])
print("policy.move", response, response.ok)  # policy.move <Response [200]> False

print("\nDeletes policy from the Fortigate by policyid (unique identifier)")
response = fgt.policy.delete(uid=policyid)
print("policy.delete", response, response.ok)  # policy.delete <Response [200]> True

print("\nDeletes policies from the Fortigate by filter (by name)")
response = fgt.policy.delete(filter="name==POLICY")
print("policy.delete", response, response.ok)  # policy.delete <Response [200]> True

print("\nChecks for absence of policy in the Fortigate")
response = fgt.policy.is_exist(uid=policyid)
print("policy.is_exist", response)  # policy.is_exist False

fgt.logout()
