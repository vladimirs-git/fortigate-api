"""Address examples.

- Create address in the Fortigate
- Get all addresses from the Fortigate
- Get filtered address by name (unique identifier)
- Filter address by operator *equals* "=="
- Filter address by operator *contains* "=@"
- Filter address by operator *not equals* "!="
- Update address data in the Fortigate
- Check for presence of address in the Fortigate
- Delete address from the Fortigate by name
- Delete addresses from the Fortigate by filter
- Check for absence of address in the Fortigate
- FortigateAPI *with* statement
"""

from pprint import pprint

from fortigate_api import FortigateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
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

print("\nFilters address by operator equals \"==\"")
addresses = fgt.address.get(filter="name==ADDRESS")
print(f"addresses count={len(addresses)}")  # addresses count=1

print("\nFilters address by operator contains \"=@\"")
addresses = fgt.address.get(filter="subnet=@127.0")
print(f"addresses count={len(addresses)}")  # addresses count=4

print("\nFilters address by operator not equals \"!=\"")
addresses = fgt.address.get(filter="name!=ADDRESS")
print(f"addresses count={len(addresses)}")  # addresses count=1726

print("\nFilters address by multiple conditions")
addresses = fgt.address.get(filter=["subnet=@127.0", "type==ipmask"])
print(f"addresses count={len(addresses)}")  # addresses count=1

print("\nUpdates address data in the Fortigate")
data = dict(name="ADDRESS", subnet="127.0.0.255 255.255.255.255", color=6)
response = fgt.address.update(uid="ADDRESS", data=data)
print("address.update", response, response.ok)  # address.update <Response [200]> True

print("\nChecks for presence of address in the Fortigate")
response = fgt.address.is_exist(uid="ADDRESS")
print("address.is_exist", response)  # address.is_exist True

print("\nDeletes address from the Fortigate by name")
response = fgt.address.delete(uid="ADDRESS")
print("address.delete", response, response.ok)  # address.delete <Response [200]> True

print("\nDeletes addresses: ADDRESS, FIREWALL_AUTH_PORTAL_ADDRESS from the Fortigate by filter. "
      "Returns <Response [500]> because FIREWALL_AUTH_PORTAL_ADDRESS cannot be deleted")
response = fgt.address.delete(filter="name=@ADDRESS")
print("address.delete", response, response.ok)  # address.delete <Response [500]> False

print("\nChecks for absence of address in the Fortigate")
response = fgt.address.is_exist(uid="ADDRESS")
print("address.is_exist", response)  # address.is_exist False

fgt.logout()

# FortigateAPI *with* statement
print("\nFortigateAPI *with* statement")
with FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD) as fgt:
    response = fgt.address.is_exist(uid="ADDRESS")
    print("address.is_exist", response)  # address.is_exist False
