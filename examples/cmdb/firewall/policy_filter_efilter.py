"""api/v2/cmdb/firewall/policy.

- Get all firewall policies, to be sure that we have some policies
- Get policies by an exact source address using Extended-filter parameter
- Get policies by an exact source address using filter parameter
"""

from fortigate_api import FortiGateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(
    host=HOST,
    username=USERNAME,
    password=PASSWORD,
)

# Get all firewall policies, to be sure that we have some policies
policies_all = api.cmdb.firewall.policy.get()
print(f"{len(policies_all)=}")  # len(policies_all)=245

# Get policies by an exact source address using Extended-filter parameter
policies_efilter = api.cmdb.firewall.policy.get(efilter=["srcaddr==1.1.1.1/32"])
print(f"{len(policies_efilter)=}")  # len(policies_efilter)=1

# Get policies by an exact source address using filter parameter
policies_filter = []
addresses = api.cmdb.firewall.address.get(filter="subnet==1.1.1.1 255.255.255.255")
for item in api.cmdb.firewall.policy.get():
    dstaddr = [d["name"] for d in item["srcaddr"]]
    for address in addresses:
        if address["name"] in dstaddr:
            policies_filter.append(item)
print(f"{len(policies_filter)=}")  # len(policies_filter)=1

api.logout()
