"""api/v2/cmdb/firewall/address

- Create address in the Fortigate
- Get all addresses from the Fortigate vdom root
- Format output data to return only required key values
- Get address by name (unique identifier)
- Filter address by operator equals `==`
- Filter address by operator contains `=@`
- Filter address by operator not equals `!=`
- Filter address by multiple conditions
- Update address data in the Fortigate
- Delete address from the Fortigate by name (unique identifier)
- Delete addresses from the Fortigate by filter
- Check for absence of address in the Fortigate
- Get all addresses from the vdom
"""

import logging
from pprint import pprint

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)
api.login()  # login is optional

# Create address in the Fortigate
data = {
    "name": "ADDRESS",
    "obj-type": "ip",
    "subnet": "127.0.0.100 255.255.255.252",
    "type": "ipmask",
}
response = api.cmdb.firewall.address.create(data)
print(f"address.create {response}")  # address.create <Response [200]>

# Get all addresses from the Fortigate vdom root
items = api.cmdb.firewall.address.get()
print(f"addresses count={len(items)}")  # addresses count=14

# Get address by name (unique identifier)
items = api.cmdb.firewall.address.get(name="ADDRESS")
print(f"addresses count={len(items)}")  # addresses count=1
pprint(items)
#  [{"comment": "",
#    "name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

# Format output data to return only required key values
items = api.cmdb.firewall.address.get(format="name|subnet")
pprint(items)
# [{"name": "ADDRESS",
#   "q_origin_key": "ADDRESS",
#   "subnet": "127.0.0.100 255.255.255.252"}]

# Filter by operator equals `==`
items = api.cmdb.firewall.address.get(filter="name==ADDRESS")
print(f"Filtered by `==`, count={len(items)}")  # Filtered by `==`, count=1

# Filter address by operator contains `=@`
items = api.cmdb.firewall.address.get(filter="subnet=@127.0")
print(f"Filtered by `=@`, count={len(items)}")  # Filtered by `=@`, count=2

# Filter address by operator not equals `!=`
items = api.cmdb.firewall.address.get(filter="name!=ADDRESS")
print(f"Filtered by `!=`, count={len(items)}")  # Filtered by `!=`, count=13

# Filter address by multiple conditions
items = api.cmdb.firewall.address.get(filter=["subnet=@127.0", "type==ipmask"])
print(f"Filtered by multiple conditions, count={len(items)}")
# Filtered by multiple conditions, count=2

# Update address data in the Fortigate
data = {"name": "ADDRESS", "subnet": "127.0.0.255 255.255.255.255"}
response = api.cmdb.firewall.address.update(data)
print(f"address.update {response}")  # address.update <Response [200]>

# Delete address from the Fortigate by name (unique identifier)
response = api.cmdb.firewall.address.delete("ADDRESS")
print(f"address.delete {response}")  # address.delete <Response [200]>

# Delete addresses from the Fortigate by filter
# Returns <Response [500]> because FIREWALL_AUTH_PORTAL_ADDRESS cannot be deleted
response = api.cmdb.firewall.address.delete(filter="name=@ADDRESS")
print(f"address.delete {response}")  # address.delete <Response [500]>

# Check for absence of address in the Fortigate
response = api.cmdb.firewall.address.is_exist("ADDRESS")
print(f"address.is_exist {response}")  # address.is_exist False

api.logout()

# Get all addresses from the vdom="VDOM9"
api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD, vdom="VDOM9")
items = api.cmdb.firewall.address.get()
print(f"addresses count={len(items)}")  # addresses count=10

api.logout()
