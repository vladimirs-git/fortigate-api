"""api/v2/cmdb/system.dhcp/server

- Create dhcp-server
- Get all dhcp-servers
- Filter dhcp-servers by id (unique identifier)
- Filter dhcp-servers by operator contains `=@`
- Filter dhcp-servers by multiple conditions
- Update dhcp-server data in the Fortigate
- Delete dhcp-server from the Fortigate by name
- Delete dhcp-servers from the Fortigate by filter
- Check for presence of dhcp-server in the Fortigate
"""

import logging
from pprint import pprint

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Create dhcp-server
data = {
    "default-gateway": "192.168.255.1",
    "netmask": "255.255.255.0",
    "interface": "port10",
    "ip-range": [{"start-ip": "192.168.255.2", "end-ip": "192.168.255.254", }],
}
response = api.cmdb.system_dhcp.server.create(data)
print("server.create", response)  # server.create <Response [200]>

# Get all dhcp-servers
items = api.cmdb.system_dhcp.server.get()
print(f"dhcp-servers count={len(items)}")  # dhcp-servers count=3

# Filter dhcp-servers by id (unique identifier)
uid = items[-1]["id"]
items = api.cmdb.system_dhcp.server.get(id=uid)
print(f"dhcp-servers {uid=} count={len(items)}")  # dhcp-servers uid=7 count=1
pprint(items)
#  [{"id": 7,
#   "interface": "port10",
#   "ip-mode": "range",
#   "ip-range": [{"end-ip": "192.168.255.254",
#                 "id": 1,
#                 "q_origin_key": 1,
#                 "start-ip": "192.168.255.2"}],
#    ...
#    }]

# Filter dhcp-servers by operator contains `=@`
items = api.cmdb.system_dhcp.server.get(filter="interface=@10")
print(f"dhcp-servers count={len(items)}")  # dhcp-servers count=1

# Filter dhcp-servers by multiple conditions
items = api.cmdb.system_dhcp.server.get(
    filter=["default-gateway==192.168.255.1", "interface=@port10"])
print(f"dhcp-servers count={len(items)}")  # dhcp-servers count=1

# Update dhcp-server data in the Fortigate
data = {"id": uid, "dns-server1": "10.0.0.1"}
response = api.cmdb.system_dhcp.server.update(data)
print("dhcp-server.update", response, response.ok)  # dhcp-server.update <Response [200]> True

# Delete dhcp-server from the Fortigate by name
response = api.cmdb.system_dhcp.server.delete(uid)
print("dhcp-server.delete", response, response.ok)  # dhcp-server.delete <Response [200]> True

# Delete dhcp-servers from the Fortigate by filter
response = api.cmdb.system_dhcp.server.delete(filter="interface==port10")
print("dhcp-server.delete", response, response.ok)  # dhcp-server.delete <Response [200]> True

# Check for presence of dhcp-server in the Fortigate
response = api.cmdb.system_dhcp.server.is_exist(uid)
print("dhcp-server.is_exist", response)  # dhcp-server.is_exist False

api.logout()
