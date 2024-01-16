"""Monitor examples.

- Get directory of monitor options (schema)
- Get all ipv4 routes
- Get static ipv4 routes
- Get route to interested ip address
"""

from pprint import pprint

from fortigate_api import FortiGate

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortiGate(host=HOST, username=USERNAME, password=PASSWORD)

# Get directory of monitor options (schema)
directory = fgt.directory("api/v2/monitor")
pprint(directory)
# [{"access_group": "sysgrp.cfg",
#   "action": "select",
#   "name": "health",
#   "path": "firewall",
#   "request": {"http_method": "GET"},
#   "response": {"type": "array"},
#   "summary": "List configured load balance server health monitors.",
#   "supported": True},
#  ...

# Get all ipv4 routes
routes = fgt.get(url="api/v2/monitor/router/ipv4")
pprint(routes)
# [{"distance": 20,
#   "gateway": "10.0.0.1",
#   "install_date": 1681965487,
#   "interface": "tunnel1",
#   "ip_mask": "10.0.0.0/8",
#   "ip_version": 4,
#   "is_tunnel_route": True,
#   "metric": 100,
#   "priority": 1,
#   "tunnel_parent": "tunnel1",
#   "type": "bgp",
#   "vrf": 0},
#   ...
# ]

# Get static ipv4 routes
routes = fgt.get(url="api/v2/monitor/router/ipv4?type=static")
pprint(routes)
# [{"distance": 10,
#   "gateway": "10.0.1.1",
#   "interface": "wan1",
#   "ip_mask": "0.0.0.0/0",
#   "ip_version": 4,
#   "metric": 0,
#   "priority": 1,
#   "type": "static",
#   "vrf": 0},
#   ...
# ]

# Get route to interested ip address
routes = fgt.get_result(url="api/v2/monitor/router/lookup?destination=10.1.1.1")
pprint(routes)
# {"gateway": "10.0.0.1",
#  "interface": "tunnel1",
#  "network": "10.0.0.0/10",
#  "success": True}
