"""api/v2/cmdb/system/global.

- Update data in the Fortigate
- Get data from the Fortigate
"""

from pprint import pprint

from fortigate_api import FortiGateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Update data in the Fortigate
data = {"timezone": 80}
response = api.cmdb.system.global_.update(data)
print(f"update {response}")  # update <Response [200]>

# Get data from the Fortigate
result = api.cmdb.system.global_.get()
pprint(result)
# [{"admin-concurrent": "enable",
#   "admin-console-timeout": 300,
#   "admin-hsts-max-age": 15552000,
#   "timezone": "80",
#   ...

api.logout()
