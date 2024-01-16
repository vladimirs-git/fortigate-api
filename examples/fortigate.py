"""FortiGate examples.

- FortiGate.post() - Create fortigate-object in the Fortigate
- FortiGate.get() - GetResponse object from the Fortigate
- FortiGate.get_results() - Get list of fortigate-objects from the JSON results section
- FortiGate.get_result() - Get single fortigate-object from the JSON results section
- FortiGate.get_list() - Get list of items from the JSON root section
- FortiGate.put() - Update existing fortigate-object in the Fortigate
- FortiGate.delete() - Delete the fortigate-object from the Fortigate
- FortiGate.exist() - Check iffortigate-object exists in the Fortigate
- Get Directory
- FortiGate `with` statement
"""

import logging
from pprint import pprint

from fortigate_api import FortiGate

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortiGate(host=HOST, username=USERNAME, password=PASSWORD)
fgt.login()  # login is optional

# FortiGate.post() - Create fortigate-object in the Fortigate
data = {
    "name": "ADDRESS",
    "obj-type": "ip",
    "subnet": "127.0.0.100 255.255.255.252",
    "type": "ipmask",
}
response = fgt.post(url="api/v2/cmdb/firewall/address/", data=data)
print(f"POST {response}", )  # POST <Response [200]>

# FortiGate.get() - GetResponse object from the Fortigate
response = fgt.get(url="api/v2/cmdb/firewall/address/ADDRESS")
print(f"GET {response}", )  # POST <Response [200]>
result = response.json()["results"]
pprint(result)
#  [{"name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

# FortiGate.get_results() - Get list of fortigate-objects from the JSON results section
items = fgt.get_results(url="api/v2/cmdb/firewall/address")
print(f"addresses count={len(items)}")  # addresses count=14

# FortiGate.get_result() - Get single fortigate-object from the JSON results section
data = fgt.get_result(url="api/v2/cmdb/alertemail/setting")
pprint(data)
# {'FDS-license-expiring-days': 15,
#  'FDS-license-expiring-warning': 'disable',
#  'FDS-update-logs': 'disable',
#  ...

# FortiGate.get_list() - Get list of items from the JSON root section
output = fgt.get_list(url="/api/v2/monitor/firewall/policy?global=1")
pprint(output)
# [{'build': 2093,
#   'http_method': 'GET',
#   'name': 'policy',
#   'path': 'firewall',
#   'results': [{'active_sessions': 0,
#                'asic_bytes': 0,
#                'asic_packets': 0,
# ...

# FortiGate.put() - Update existing fortigate-object in the Fortigate
data = {"name": "ADDRESS", "subnet": "127.0.0.255 255.255.255.255"}
response = fgt.put(url="api/v2/cmdb/firewall/address/ADDRESS", data=data)
print(f"PUT {response}")  # PUT <Response [200]>

# FortiGate.delete() - Delete the fortigate-object from the Fortigate
response = fgt.delete(url="api/v2/cmdb/firewall/address/ADDRESS")
print(f"DELETE {response}", )  # DELETE <Response [200]>

# FortiGate.exist() - Check iffortigate-object exists in the Fortigate
response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
print(f"exist {response}", )  # exist <Response [404]>

# Get Directory
output = fgt.directory(url="/api/v2/log")
pprint(output)
output = fgt.directory(url="/api/v2/monitor")
pprint(output)

fgt.logout()

# FortiGate `with` statement
with FortiGate(host=HOST, username=USERNAME, password=PASSWORD) as fgt:
    response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
    print("exist", response)  # exist <Response [404]>
