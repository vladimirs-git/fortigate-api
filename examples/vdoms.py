"""Vdoms example."""

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

fgt.logout()
