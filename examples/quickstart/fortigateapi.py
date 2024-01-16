"""Quickstart FortiGateAPI.

- Create address in the Fortigate
- Get all addresses from the Fortigate vdom root
- Get address by name (unique identifier)
- Filter address by operator contains `=@`
- Update address data in the Fortigate
- Delete address from the Fortigate
"""

import logging
from pprint import pprint

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

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
print(f"All addresses count={len(items)}")  # All addresses count=14

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

# Filter address by operator contains `=@`
items = api.cmdb.firewall.address.get(filter="subnet=@127.0")
print(f"Filtered by `=@`, count={len(items)}")  # Filtered by `=@`, count=2

# Update address data in the Fortigate
data = {"name": "ADDRESS", "subnet": "127.0.0.255 255.255.255.255"}
response = api.cmdb.firewall.address.update(data)
print(f"address.update {response}")  # address.update <Response [200]>

# Delete address from the Fortigate
response = api.cmdb.firewall.address.delete("ADDRESS")
print(f"address.delete {response}")  # address.delete <Response [200]>

api.logout()
