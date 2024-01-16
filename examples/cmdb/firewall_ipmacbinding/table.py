"""api/v2/cmdb/firewall.ipmacbinding/table

- Create table in the Fortigate
- Get all tables from the Fortigate
- Get filtered table by seq-num (unique identifier)
- Update table data in the Fortigate
- Delete table from the Fortigate by seq-num (unique identifier)
- Check for absence of table in the Fortigate
"""

import logging

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Create table in the Fortigate
data = {
    "name": "TABLE",
    "ip": "10.0.0.1",
    "mac": "00:00:00:00:00:01",
    "status": "enable",
}
response = api.cmdb.firewall_ipmacbinding.table.create(data)
print("table.create", response)  # table.create <Response [200]>

# Get all tables from the Fortigate
items = api.cmdb.firewall_ipmacbinding.table.get()
print(f"tables count={len(items)}")  # tables count=1

# Get filtered table by seq-num (unique identifier)
items = api.cmdb.firewall_ipmacbinding.table.get(**{"seq-num": 1})
print(f"tables count={len(items)}")  # tables count=1

# Update table data in the Fortigate
seq_num = items[0]["seq-num"]
data = {"seq-num": seq_num, "mac": "00:00:00:00:00:02"}
response = api.cmdb.firewall_ipmacbinding.table.update(data)
print("table.update", response)  # table.update <Response [200]>

# Delete table from the Fortigate by seq-num (unique identifier)
response = api.cmdb.firewall_ipmacbinding.table.delete(seq_num)
print("table.delete", response)  # table.delete <Response [200]>

# Check for absence of table in the Fortigate
response = api.cmdb.firewall_ipmacbinding.table.is_exist(seq_num)
print("table.is_exist", response)  # table.is_exist False

api.logout()
