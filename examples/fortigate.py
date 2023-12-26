"""Fortigate examples.

- User-Based Authentication,
- Create address in the Fortigate,
- Get address by name (unique identifier) from the Fortigate,
- Update address data in the Fortigate,
- Check for presence of address in the Fortigate,
- Delete address from the Fortigate by name (unique identifier),
- Check for absence of address in the Fortigate,
- Get logs traffic forward, value in JSON section with key="results",
- Get monitor policy, value in JSON root section,
- Get Directory
- Fortigate `with` statement,
"""

import logging
from pprint import pprint

from fortigate_api import Fortigate

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = Fortigate(host=HOST, username=USERNAME, password=PASSWORD)

# Creates address in the Fortigate
data = {
    "name": "ADDRESS",
    "obj-type": "ip",
    "subnet": "127.0.0.100 255.255.255.252",
    "type": "ipmask",
}
response = fgt.post(url="api/v2/cmdb/firewall/address/", data=data)
print(f"POST {response}", )  # POST <Response [200]>

# Get address by name (unique identifier) from the Fortigate
addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
addresses = [d for d in addresses if d["name"] == "ADDRESS"]
pprint(addresses)
#  [{"comment": "",
#    "name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

# Updates address data in the Fortigate
data = dict(color=6)
response = fgt.put(url="api/v2/cmdb/firewall/address/ADDRESS", data=data)
print(f"PUT {response}")  # PUT <Response [200]>

# Delete address from the Fortigate by name (unique identifier)
response = fgt.delete(url="api/v2/cmdb/firewall/address/ADDRESS")
print(f"DELETE {response}", )  # DELETE <Response [200]>

# Checks for absence of address in the Fortigate
response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
print(f"Exist {response}", )  # Exist <Response [404]>

# Get logs traffic forward, value in JSON section with key="results"
output = fgt.get(url="/api/v2/log/memory/traffic/forward")
pprint(output)
# [{'_metadata': {'#': 1, 'archive': False, 'logid': 13, 'roll': 63501, ...},
#   'action': 'deny',
#   'appcat': 'unscanned',
#   'craction': 131072,
#   'crlevel': 'high',
#   'crscore': 30,
# ...

# Get monitor policy, value in JSON root section
output = fgt.get_l(url="/api/v2/monitor/firewall/policy?global=1")
pprint(output)
# [{'build': 2093,
#   'http_method': 'GET',
#   'name': 'policy',
#   'path': 'firewall',
#   'results': [{'active_sessions': 0,
#                'asic_bytes': 0,
#                'asic_packets': 0,
# ...


# Get Directory
output = fgt.directory(url="/api/v2/log")
pprint(output)
output = fgt.directory(url="/api/v2/monitor")
pprint(output)

fgt.logout()

# Fortigate `with` statement
with Fortigate(host=HOST, username=USERNAME, password=PASSWORD) as fgt:
    response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
    print("Exist", response)  # Exist <Response [404]>
