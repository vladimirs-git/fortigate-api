"""External Resources examples.

- Create external_resource in the Fortigate
- Get all external_resources from the Fortigate
- Get filtered external_resource by name (unique identifier)
- Filter external_resource by operator *equals* "=="
- Filter external_resource by operator *contains* "=@"
- Filter external_resource by operator *not equals* "!="
- Update external_resource data in the Fortigate
- Check for presence of external_resource in the Fortigate
- Delete external_resource from the Fortigate by name
- Check for absence of external_resource in the Fortigate
"""

from pprint import pprint

from fortigate_api import FortigateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
fgt.login()

# Create External Resources
data = {
    "name": "EXTERNAL_RESOURCE_NAME",
    "resource": "https://domain.com/resource.txt",
    "type": "address",
}
response = fgt.external_resource.create(data=data)
print("external_resource.create", response)  # external_resource.create <Response [200]>

print("\nGets all external resources from the Fortigate")
external_resources = fgt.external_resource.get()
print(f"external_resources count={len(external_resources)}")  # external_resources count=5

print("\nGets filtered external_resource by name (unique identifier)")
external_resources = fgt.external_resource.get(uid="EXTERNAL_RESOURCE_NAME")
pprint(external_resources)
#  [{"category": 0,
#    "name": "EXTERNAL_RESOURCE_NAME",
#    "resource": "https://domain.com/resource.txt",
#    ...
#    }]

print("\nFilters external_resource by operator equals \"==\"")
external_resources = fgt.external_resource.get(filter="name==EXTERNAL_RESOURCE_NAME")
print(f"external_resources count={len(external_resources)}")  # external_resources count=1

print("\nFilters external_resource by operator contains \"=@\"")
external_resources = fgt.external_resource.get(filter="resource=@domain.com")
print(f"external_resources count={len(external_resources)}")  # external_resources count=2

print("\nFilters external_resource by operator not equals \"!=\"")
external_resources = fgt.external_resource.get(filter="name!=EXTERNAL_RESOURCE_NAME")
print(f"external_resources count={len(external_resources)}")  # external_resources count=4

print("\nFilters external_resource by multiple conditions")
external_resources = fgt.external_resource.get(filter=["resource=@domain.com", "type==address"])
print(f"external_resources count={len(external_resources)}")  # external_resources count=2

print("\nUpdates external_resource data in the Fortigate")
data = dict(name="EXTERNAL_RESOURCE_NAME", status="disable")
response = fgt.external_resource.update(uid="EXTERNAL_RESOURCE_NAME", data=data)
print("external_resource.update", response)  # external_resource.update <Response [200]>

print("\nChecks for presence of external_resource in the Fortigate")
response = fgt.external_resource.is_exist(uid="EXTERNAL_RESOURCE_NAME")
print("external_resource.is_exist", response)  # external_resource.is_exist True

print("\nDeletes external_resource from the Fortigate by name")
response = fgt.external_resource.delete(uid="EXTERNAL_RESOURCE_NAME")
print("external_resource.delete", response)  # external_resource.delete <Response [200]>

print("\nChecks for absence of external_resource in the Fortigate")
response = fgt.external_resource.is_exist(uid="EXTERNAL_RESOURCE_NAME")
print("external_resource.is_exist", response)  # external_resource.is_exist False

fgt.logout()
