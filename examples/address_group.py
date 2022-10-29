"""AddressGroup examples:

- Creates address-group in the Fortigate
- Gets all address-groups from the Fortigate
- Gets filtered address-group by name (unique identifier)
- Filters address-group by operator *equals* "=="
- Filters address-group by operator *contains* "=@"
- Filters address-group by operator *not equals* "!="
- Updates address-group data in the Fortigate
- Checks for presence of address-group in the Fortigate
- Deletes address-group from the Fortigate by name
- Deletes address-groups from the Fortigate by filter
- Checks for absence of address-group in the Fortigate
"""

from pprint import pprint

from fortigate_api import FortigateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
fgt.login()

print("\nCreates address and address-group in the Fortigate")
data = {"name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.255",
        "type": "ipmask"}
response = fgt.address.create(data=data)
print("address.create", response)  # address.create <Response [200]>
data = {"name": "ADDR_GROUP", "member": [{"name": "ADDRESS"}]}
response = fgt.address_group.create(data=data)
print("address_group.creat", response)  # address_group.creat <Response [200]>

print("\nGets all address-groups from the Fortigate")
address_groups = fgt.address_group.get()
print(f"address_groups count={len(address_groups)}")  # address_groups count=115

print("\nGets filtered address_group by name (unique identifier)")
address_groups = fgt.address_group.get(uid="ADDR_GROUP")
pprint(address_groups)
#  [{"comment": "",
#    "name": "ADDR_GROUP",
#    "member": [{"name": "ADDRESS", "q_origin_key": "ADDRESS"}],
#    "uuid": "d346aeca-d76a-51ec-7005-541cf3b816f5",
#    ...
#    }]

print("\nFilters address_group by operator equals \"==\"")
address_groups = fgt.address_group.get(filter="name==ADDR_GROUP")
print(f"address_groups count={len(address_groups)}")  # address_groups count=1

print("\nFilters address_group by operator contains \"=@\"")
address_groups = fgt.address_group.get(filter="name=@MS")
print("address_groups count", len(address_groups))  # address_groups count 6

print("\nFilters address_group by operator not equals \"!=\"")
address_groups = fgt.address_group.get(filter="name!=ADDR_GROUP")
print(f"address_groups count={len(address_groups)}")  # address_groups count=114

print("\nFilters address_group by multiple conditions")
address_groups = fgt.address_group.get(filter=["name=@MS", "color==6"])
print(f"address_groups count={len(address_groups)}")  # address_groups count=2

print("\nUpdates address_group data in the Fortigate")
data = dict(name="ADDR_GROUP", color=6)
response = fgt.address_group.update(uid="ADDR_GROUP", data=data)
print("address_group.update", response)  # address_group.update <Response [200]>

print("\nChecks for presence of address_group in the Fortigate")
response = fgt.address_group.is_exist(uid="ADDR_GROUP")
print("address_group.is_exist", response)  # address_group.is_exist True

print("\nDeletes address_group from the Fortigate by name")
response = fgt.address_group.delete(uid="ADDR_GROUP")
print("address_group.delete", response)  # address_group.delete <Response [200]>

print("\nDeletes address_groups by filter by filter")
response = fgt.address_group.delete(filter="name=@ADDR_GROUP")
print("address_group.delete", response)  # address_group.delete <Response [200]>

print("\nDeletes address object")
response = fgt.address.delete(uid="ADDRESS")
print("address.delete", response)  # address.delete <Response [200]>

print("\nChecks for absence of address_group in the Fortigate")
response = fgt.address_group.is_exist(uid="ADDR_GROUP")
print("address_group.is_exist", response)  # address_group.is_exist False

fgt.logout()
