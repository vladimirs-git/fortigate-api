"""api/v2/cmdb/system.snmp/community.

- Creates snmp-community
- Get all snmp-community
- Filter snmp-community by operator equals `==`
- Filter snmp-community by id (unique identifier)
- Filter snmp-community by multiple conditions
- Update snmp-community data in the Fortigate
- Delete snmp-community from the Fortigate by name
- Delete snmp-community from the Fortigate by filter
- Check for presence of snmp-community in the Fortigate
"""

from fortigate_api import FortiGateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Creates snmp-community
data = {"name": "SNMP_COMMUNITY", "hosts": [{"id": 1, "ip": "10.0.0.0 255.0.0.0"}]}
response = api.cmdb.system_snmp.community.create(data=data)
print("community.create", response)  # community.create <Response [200]>

# Get all snmp-community
items = api.cmdb.system_snmp.community.get()
print(f"community count={len(items)}")  # community count=3

# Filter snmp-community by operator equals `==`
items = api.cmdb.system_snmp.community.get(filter="name==SNMP_COMMUNITY")
print(f"community count={len(items)}")  # community count=1

# Filter snmp-community by id (unique identifier)
uid = items[-1]["id"]
items = api.cmdb.system_snmp.community.get(id=uid)
print(f"community count={len(items)}")  # community count=1

# Filter snmp-community by multiple conditions
filters = ["name==SNMP_COMMUNITY", "query-v2c-status==enable"]
items = api.cmdb.system_snmp.community.get(filter=filters)
print(f"community count={len(items)}")  # community count=1

# Update snmp-community data in the Fortigate
data = {"id": uid, "query-v2c-status": "disable"}
response = api.cmdb.system_snmp.community.update(data)
print("community.update", response)  # community.update <Response [200]>

# Delete snmp-community from the Fortigate by name
response = api.cmdb.system_snmp.community.delete(uid)
print("community.delete", response)  # community.delete <Response [200]>

# Delete snmp-community from the Fortigate by filter
response = api.cmdb.system_snmp.community.delete(filter="name=@SNMP_")
print("community.delete", response)  # community.delete <Response [404]>

# Check for presence of snmp-community in the Fortigate
response = api.cmdb.system_snmp.community.is_exist(uid)
print("community.is_exist", response)  # community.is_exist False

api.logout()
