"""Address examples.

- Token-Based Authentication
- Create address in the Fortigate
- Get all addresses from the Fortigate
- Delete address from the Fortigate
"""

import logging
from pprint import pprint

from fortigate_api import FortigateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
TOKEN = "token"

fgt = FortigateAPI(host=HOST, token=TOKEN)
fgt.login()

# Create Address
data = {"name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.252",
        "type": "ipmask"}
response = fgt.address.create(data=data)
print("address.create", response)  # address.create <Response [200]>

print("\nGets all addresses from the Fortigate")
addresses = fgt.address.get()
print(f"addresses count={len(addresses)}")  # addresses count=1727

print("\nGets filtered address by name (unique identifier)")
addresses = fgt.address.get(uid="ADDRESS")
pprint(addresses)
#  [{"comment": "",
#    "name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

print("\nDeletes address from the Fortigate by name")
response = fgt.address.delete(uid="ADDRESS")
print("address.delete", response, response.ok)  # address.delete <Response [200]> True

fgt.logout()
