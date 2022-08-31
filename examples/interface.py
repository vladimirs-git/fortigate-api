"""Examples Interface"""

from pprint import pprint

from fortigate_api import FortigateAPI

fgt = FortigateAPI(host="host", username="username", password="password")
fgt.login()

print("\nGets all interfaces in vdom \"root\" from Fortigate")
interfaces = fgt.interface.get()
print(f"interfaces count={len(interfaces)}")  # interfaces count=21

print("\nGets filtered interface by name (unique identifier)")
interfaces = fgt.interface.get(uid="dmz")
pprint(interfaces)
#  [{"name": "dmz",
#    "ip": "0.0.0.0 0.0.0.0",
#    ...
#    }]

print("\nFilters interface by operator equals \"==\"")
interfaces = fgt.interface.get(filter="name==dmz")
print(f"interfaces count={len(interfaces)}")  # interfaces count=1

print("\nFilters interface by operator contains \"=@\"")
interfaces = fgt.interface.get(filter="name=@wan")
print(f"interfaces count={len(interfaces)}")  # interfaces count=2

print("\nFilters interface by operator not equals \"!=\"")
interfaces = fgt.interface.get(filter="name!=dmz")
print(f"interfaces count={len(interfaces)}")  # interfaces count=20

print("\nFilters interface by multiple conditions")
interfaces = fgt.interface.get(filter=["allowaccess=@ping", "detectprotocol==ping"])
print(f"interfaces count={len(interfaces)}")  # interfaces count=8

print("\nUpdates interface data in the Fortigate")
data = dict(name="dmz", description="dmz")
response = fgt.interface.update(uid="dmz", data=data)
print("interface.update", response)  # interface.update <Response [200]>

print("\nChecks for presence of interface in the Fortigate")
response = fgt.interface.is_exist(uid="dmz")
print("interface.is_exist", response)  # interface.is_exist True

print("\nChanges virtual domain to \"VDOM\" and gets all interfaces inside this vdom")
fgt.fgt.vdom = "VDOM"
print(f"{fgt!r}")  # Fortigate(host='host', username='username', password='********', vdom='VDOM')
print(fgt.vdom)  # VDOM
interfaces = fgt.interface.get()
print(f"interfaces count={len(interfaces)}")  # interfaces count=0

print("\nChanges virtual domain to \"root\"")
fgt.vdom = "root"
print(f"{fgt!r}")  # Fortigate(host='host', username='username', password='********')
print(fgt.vdom)  # root

fgt.logout()
