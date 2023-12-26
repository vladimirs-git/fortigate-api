"""Quickstart.

:py:class:`.FortigateAPI` demonstration.

- Create address in the Fortigate,
- Get all addresses from the Fortigate,
- Get filtered address by name (unique identifier),
- Filter address by operator *contains* `=@`,
- Update address data in the Fortigate,
- Delete address from the Fortigate by name (unique identifier),
- Check for absence of address in the Fortigate,
"""

import logging
from pprint import pprint

from fortigate_api import FortigateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Create address in the Fortigate
data = {
    "name": "ADDRESS",
    "obj-type": "ip",
    "subnet": "127.0.0.100 255.255.255.252",
    "type": "ipmask",
}
response = fgt.address.create(data)
print(f"address.create {response}")  # address.create <Response [200]>

# Get all addresses from the Fortigate
addresses = fgt.address.get()
print(f"All addresses count={len(addresses)}")  # All addresses count=14

# Get filtered address by name (unique identifier)
addresses = fgt.address.get(uid="ADDRESS")
pprint(addresses)
#  [{"comment": "",
#    "name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

# Filter address by operator *contains* `=@`
addresses = fgt.address.get(filter="subnet=@127.0")
print(f"Filtered by `=@`, count={len(addresses)}")  # Filtered by `=@`, count=2

# Update address data in the Fortigate
data = dict(name="ADDRESS", subnet="127.0.0.255 255.255.255.255", color=6)
response = fgt.address.update(uid="ADDRESS", data=data)
print(f"address.update {response}")  # address.update <Response [200]>

# Delete address from the Fortigate by name (unique identifier)
response = fgt.address.delete(uid="ADDRESS")
print(f"address.delete {response}")  # address.delete <Response [200]>

# Check for absence of address in the Fortigate
response = fgt.address.is_exist(uid="ADDRESS")
print(f"address.is_exist {response}")  # address.is_exist False

fgt.logout()



