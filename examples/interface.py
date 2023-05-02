"""Interface examples.

- Get all interfaces in vdom "root" from the Fortigate
- Get filtered interface by name (unique identifier)
- Filter interface by operator *equals* "=="
- Filter interface by operator contains "=@"
- Filter interface by operator *not equals* "!="
- Filter interface by multiple conditions
- Update interface data in the Fortigate
- Check for presence of interface in the Fortigate
- Change virtual domain to VDOM and get all interfaces of this virtual domain
- Change virtual domain to root and get all interfaces of this virtual domain
- Get all interfaces in all virtual domains (root and VDOM)
"""

import logging
from pprint import pprint

from fortigate_api import FortigateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
fgt.login()

print("\nGet all interfaces in vdom \"root\" from the Fortigate")
interfaces = fgt.interface.get()
print(f"interfaces count={len(interfaces)}")  # interfaces count=21

print("\nGet filtered interface by name (unique identifier)")
interfaces = fgt.interface.get(uid="dmz")
pprint(interfaces)
#  [{"name": "dmz",
#    "ip": "0.0.0.0 0.0.0.0",
#    ...
#    }]

print("\nFilter interface by operator equals \"==\"")
interfaces = fgt.interface.get(filter="name==dmz")
print(f"interfaces count={len(interfaces)}")  # interfaces count=1

print("\nFilter interface by operator contains \"=@\"")
interfaces = fgt.interface.get(filter="name=@wan")
print(f"interfaces count={len(interfaces)}")  # interfaces count=2

print("\nFilter interface by operator not equals \"!=\"")
interfaces = fgt.interface.get(filter="name!=dmz")
print(f"interfaces count={len(interfaces)}")  # interfaces count=20

print("\nFilter interface by multiple conditions")
interfaces = fgt.interface.get(filter=["allowaccess=@ping", "detectprotocol==ping"])
print(f"interfaces count={len(interfaces)}")  # interfaces count=8

print("\nUpdate interface data in the Fortigate")
data = dict(name="dmz", description="dmz")
response = fgt.interface.update(uid="dmz", data=data)
print("interface.update", response)  # interface.update <Response [200]>

print("\nCheck for presence of interface in the Fortigate")
response = fgt.interface.is_exist(uid="dmz")
print("interface.is_exist", response)  # interface.is_exist True

# Interfaces in virtual domains

print("\nChange virtual domain to VDOM and get all interfaces of this virtual domain")
fgt.rest.vdom = "VDOM"
print(f"{fgt!r}")  # Fortigate(host='host', username='username', vdom='VDOM')
print(fgt.vdom)  # VDOM
interfaces = fgt.interface.get()
print(f"interfaces count={len(interfaces)}")  # interfaces count=12

print("\nChange virtual domain to root and get all interfaces of this virtual domain")
fgt.vdom = "root"
print(f"{fgt!r}")  # Fortigate(host='host', username='username')
print(fgt.vdom)  # root
interfaces = fgt.interface.get()
print(f"interfaces count={len(interfaces)}")  # interfaces count=31

print("\nGet all interfaces in all virtual domains (root and VDOM)")
interfaces = fgt.interface.get(all=True)
print(f"interfaces count={len(interfaces)}")  # interfaces count=43

fgt.logout()
