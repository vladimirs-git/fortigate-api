"""api/v2/cmdb/system/vdom

- Create vdom in the Fortigate
- Get all vdoms from the Fortigate
- Get vdom by name (unique identifier)
- Delete vdom from the Fortigate
- Check for presence of vdom in the Fortigate
"""

import logging
from pprint import pprint

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Create vdom in the Fortigate
data = {"name": "VDOM1"}
response = api.cmdb.system.vdom.create(data)
print(f"vdom.create {response}")  # vdoms.create <Response [200]>

# Get all vdoms from the Fortigate
items = api.cmdb.system.vdom.get()
print(f"vdoms count={len(items)}")  # vdoms count=3

# Get vdom by name (unique identifier)
items = api.cmdb.system.vdom.get(name="VDOM1")
print(f"vdoms count={len(items)}")  # vdoms count=1
pprint(items)
#  [{'flag': 0,
#   'name': 'VDOM1',
#   'q_origin_key': 'VDOM1',
#   'short-name': 'VDOM1',
#   'vcluster-id': 0}]

# Delete vdom from the Fortigate
response = api.cmdb.system.vdom.delete("VDOM1")
print(f"vdom.delete {response}")  # vdoms.delete <Response [200]>

# Check for presence of vdom in the Fortigate
response = api.cmdb.system.vdom.is_exist("VDOM1")
print("vdom.is_exist", response)  # vdom.is_exist False

api.logout()
