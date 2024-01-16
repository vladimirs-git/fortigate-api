"""api/v2/cmdb/firewall.ipmacbinding/settings

- Get setting from the Fortigate
- Format output data to return only required key values
"""

import logging
from pprint import pprint

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)

# Get setting from the Fortigate
items = api.cmdb.firewall_ipmacbinding.setting.get()
pprint(items)
#  [{'bindthroughfw': 'disable', 'bindtofw': 'disable', 'undefinedhost': 'block'}]

# Format output data to return only required key values
items = api.cmdb.firewall_ipmacbinding.setting.get(format="bindthroughfw|bindtofw")
pprint(items)
# [{'bindthroughfw': 'disable', 'bindtofw': 'disable'}]

api.logout()
