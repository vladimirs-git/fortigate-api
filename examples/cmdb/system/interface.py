"""api/v2/cmdb/system/interface.

- Get all interfaces from the vdom="VDOM9"
- Get all interfaces from the vdom="root"
- Get all interfaces from the all vdoms
- Get filtered interface by name (unique identifier)
- Update interface data in the Fortigate
- Check for presence of interface in the Fortigate
"""

from pprint import pprint

from fortigate_api import FortiGateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

# Get all interfaces from the vdom="VDOM9"
api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD, vdom="VDOM9")
items = api.cmdb.system.interface.get()
print(f"interfaces count={len(items)}")  # interfaces count=2

# Get all interfaces from the vdom="root"
api.vdom = "root"
items = api.cmdb.system.interface.get()
print(f"interfaces count={len(items)}")  # interfaces count=38

# Get all interfaces from the all vdoms
items = api.cmdb.system.interface.get(all_vdoms=True)
print(f"interfaces count={len(items)}")  # interfaces count=40

# Get filtered interface by name (unique identifier)
items = api.cmdb.system.interface.get(name="dmz")
print(f"interfaces count={len(items)}")  # interfaces count=1
pprint(items)
#  [{"name": "dmz",
#    "ip": "0.0.0.0 0.0.0.0",
#    ...
#    }]

# Filter interface by operator equals `==`
items = api.cmdb.system.interface.get(filter="name==dmz")
print(f"interfaces count={len(items)}")  # interfaces count=1

# Filter interface by operator contains `=@`
items = api.cmdb.system.interface.get(filter="name=@wan")
print(f"interfaces count={len(items)}")  # interfaces count=2

# Filter interface by multiple conditions
items = api.cmdb.system.interface.get(filter=["allowaccess=@ping", "detectprotocol==ping"])
print(f"interfaces count={len(items)}")  # interfaces count=12

# Update interface data in the Fortigate
data = dict(name="dmz", description="dmz")
response = api.cmdb.system.interface.update(data)
print("interface.update", response)  # interface.update <Response [200]>

# Check for presence of interface in the Fortigate
response = api.cmdb.system.interface.is_exist("dmz")
print("interface.is_exist", response)  # interface.is_exist True

api.logout()
