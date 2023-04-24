"""SnmpCommunity examples."""

import logging
from pprint import pprint

from fortigate_api import FortigateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
fgt.login()

print("\nCreates snmp_community")
data = {
    "name": "SNMP_COMMUNITY",
    "hosts": [{"id": 1, "ip": "10.0.0.0 255.0.0.0"}],
}
response = fgt.snmp_community.create(data=data)
print("snmp_community.create", response)  # snmp_community.create <Response [200]>

print("\nGets all snmp_community")
snmp_community = fgt.snmp_community.get()
print(f"snmp_community count={len(snmp_community)}")  # snmp_community count=3

print("\nFilters snmp_community by id (unique identifier)")
snmp_community = fgt.snmp_community.get(uid="3")
pprint(snmp_community)
#  [{"id": 3,
#   "name": "SNMP_COMMUNITY",
#    ...
#    }]

print("\nFilters snmp_community by operator equals \"==\"")
snmp_community = fgt.snmp_community.get(filter="name==SNMP_COMMUNITY")
print(f"snmp_community count={len(snmp_community)}")  # snmp_community count=1

print("\nFilters snmp_community by operator contains \"=@\"")
snmp_community = fgt.snmp_community.get(filter="name=@SNMP_")
print(f"snmp_community count={len(snmp_community)}")  # snmp_community count=1

print("\nFilters snmp_community by operator not equals \"!=\"")
snmp_community = fgt.snmp_community.get(filter="name!=SNMP_COMMUNITY")
print(f"snmp_community count={len(snmp_community)}")  # snmp_community count=2

print("\nFilters snmp_community by multiple conditions")
snmp_community = fgt.snmp_community.get(filter=["name==SNMP_COMMUNITY", "query-v2c-status==enable"])
print(f"snmp_community count={len(snmp_community)}")  # snmp_community count=1

print("\nUpdates snmp_community data in the Fortigate")
data = {"name": "SNMP_COMMUNITY", "query-v2c-status": "disable"}
response = fgt.snmp_community.update(uid="3", data=data)
print("snmp_community.update", response, response.ok)  # snmp_community.update <Response [200]> True

print("\nChecks for presence of snmp_community in the Fortigate")
response = fgt.snmp_community.is_exist(uid="3")
print("snmp_community.is_exist", response)  # snmp_community.is_exist True

print("\nDeletes snmp_community from the Fortigate by name")
response = fgt.snmp_community.delete(uid="3")
print("snmp_community.delete", response, response.ok)  # snmp_community.delete <Response [200]> True

print("\nDeletes snmp_community from the Fortigate by filter")
response = fgt.snmp_community.delete(filter="name=@SNMP_")
print("snmp_community.delete", response, response.ok)  # snmp_community.delete <Response [200]> True

fgt.logout()
