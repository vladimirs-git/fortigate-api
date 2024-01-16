"""api/v2/cmdb/firewall/addrgrp

- Creates address and address-group in the Fortigate
- Get all address-groups from the Fortigate vdom root
- Get filtered address-groups by name (unique identifier)
- Filter address-groups by operator contains `=@`
- Filter address-groups by multiple conditions
- Update address-groups data in the Fortigate
- Delete address-groups from the Fortigate by name
- Delete address-groups by filter
- Delete address object
- Check for absence of address-groups in the Fortigate
"""

import logging

from fortigate_api import FortiGateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD, logging_error=True)
api.login()  # login is optional

# Creates address and address-group in the Fortigate
data = {"name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.255",
        "type": "ipmask"}
response = api.cmdb.firewall.address.create(data)
print("address.create", response)  # address.create <Response [200]>
data = {
    "name": "ADDR_GROUP",
    "member": [{"name": "ADDRESS"}],
}
response = api.cmdb.firewall.addrgrp.create(data)
print("addrgrp.creat", response)  # addrgrp.creat <Response [200]>

# Get all address-groups from the Fortigate vdom root
items = api.cmdb.firewall.addrgrp.get()
print(f"addrgrp count={len(items)}")  # addrgrp count=115

# Get filtered address-groups by name (unique identifier)
items = api.cmdb.firewall.addrgrp.get(name="ADDR_GROUP")
print(f"addrgrp count={len(items)}")  # addrgrp count=1

# Filter address-groups by operator contains `=@`
items = api.cmdb.firewall.addrgrp.get(filter="name=@MS")
print("addrgrp count", len(items))  # addrgrp count 6

# Filter address-groups by multiple conditions
items = api.cmdb.firewall.addrgrp.get(filter=["name=@MS", "color==6"])
print(f"addrgrp count={len(items)}")  # addrgrp count=2

# Update address-groups data in the Fortigate
data = dict(name="ADDR_GROUP", color=6)
response = api.cmdb.firewall.addrgrp.update(data)
print("addrgrp.update", response)  # addrgrp.update <Response [200]>

# Delete address-groups from the Fortigate by name
response = api.cmdb.firewall.addrgrp.delete("ADDR_GROUP")
print("addrgrp.delete", response)  # addrgrp.delete <Response [200]>

# Delete address-groups by filter
response = api.cmdb.firewall.addrgrp.delete(filter="name=@ADDR_GROUP")
print("addrgrp.delete", response)  # addrgrp.delete <Response [404]>

# Delete address object
response = api.cmdb.firewall.address.delete("ADDRESS")
print("address.delete", response)  # address.delete <Response [200]>

# Check for absence of address-groups in the Fortigate
response = api.cmdb.firewall.addrgrp.is_exist("ADDR_GROUP")
print("addrgrp.is_exist", response)  # addrgrp.is_exist False

api.logout()
