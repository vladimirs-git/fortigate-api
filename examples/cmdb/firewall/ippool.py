"""api/v2/cmdb/firewall/ippool

- Creates ip-pool in the Fortigate
- Get all ip-pools from the Fortigate vdom root
- Get filtered ip-pools by name (unique identifier)
- Update ip-pool data in the Fortigate
- Delete ip-pool from the Fortigate by name
- Check for presence of ip-pool in the Fortigate
"""

import logging

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Creates ip-pool in the Fortigate
data = {"name": "IP_POOL1", "startip": "10.0.0.1", "endip": "10.0.0.2"}
response = api.cmdb.firewall.ippool.create(data)
print("ip-pool.create", response)  # address.create <Response [200]>

# Get all ip-pools from the Fortigate vdom root
items = api.cmdb.firewall.ippool.get()
print(f"ip-pools count={len(items)}")  # ip-pools count=2

# Get filtered ip-pools by name (unique identifier)
items = api.cmdb.firewall.ippool.get(name="IP_POOL1")
print(f"ip-pools count={len(items)}")  # ip-pools count=2

# Update ip-pool data in the Fortigate
data = dict(name="IP_POOL1", comments="description")
response = api.cmdb.firewall.ippool.update(data)
print("ip-pool.update", response)  # ip-pool.update <Response [200]>

# Delete ip-pool from the Fortigate by name
response = api.cmdb.firewall.ippool.delete("IP_POOL1")
print("ip-pool.delete", response)  # addrgrp.delete <Response [200]>

# Check for presence of ip-pool in the Fortigate
response = api.cmdb.firewall.ippool.is_exist("IP_POOL1")
print("ip_pool.is_exist", response)  # ip_pool.is_exist False

api.logout()
