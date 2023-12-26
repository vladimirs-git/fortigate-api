"""Vdoms example.

- Create vdom in the Fortigate,
- Get all vdoms from the Fortigate,
- Get vdom by name (unique identifier),
- Delete vdom from the Fortigate,
"""

import logging
from pprint import pprint

from fortigate_api import FortigateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)

fgt.login()

print("\nGets all vdoms from the Fortigate")
vdoms = fgt.vdoms.get()
pprint(vdoms)
#[{'flag': 0,
#  'name': 'TEST1',
#  'q_origin_key': 'TEST1',
#  'short-name': 'TEST1',
#  'vcluster-id': 0},
#{'flag': 0,
#  'name': 'TEST2',
#  'q_origin_key': 'TEST2',
#  'short-name': 'TEST2',
#  'vcluster-id': 0}]
=======

# Create vdom in the Fortigate
data = {
    "name": "VDOM1",
}
response = fgt.vdoms.create(data)
print(f"vdoms.create {response}")  # vdoms.create <Response [200]>

# Get all vdoms from the Fortigate
vdoms = fgt.vdoms.get()
pprint(vdoms)
# [{'flag': 0,
#   'name': 'VDOM1',
#   'q_origin_key': 'VDOM1',
#   'short-name': 'VDOM1',
#   'vcluster-id': 0},
#  {'flag': 0,
#   'name': 'root',
#   'q_origin_key': 'root',
#   'short-name': 'root',
#   'vcluster-id': 0}]

# Get vdom by name (unique identifier)
vdoms = fgt.vdoms.get(uid="VDOM1")
pprint(vdoms)
#  [{'flag': 0,
#   'name': 'VDOM1',
#   'q_origin_key': 'VDOM1',
#   'short-name': 'VDOM1',
#   'vcluster-id': 0}]

# Delete vdom from the Fortigate
response = fgt.vdoms.delete(uid="VDOM1")
print(f"vdoms.delete {response}")  # vdoms.delete <Response [200]>

fgt.logout()