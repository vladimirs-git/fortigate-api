"""Examples Fortigate"""

from pprint import pprint

from fortigate_api import Fortigate

fgt = Fortigate(host="host", username="username", password="password")
fgt.login()

# Creates address in the Fortigate
data = {"name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.252",
        "type": "ipmask"}
response = fgt.post(url="api/v2/cmdb/firewall/address/", data=data)
print("post", response)  # post <Response [200]>

print("\nGets address data from Fortigate")
addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
addresses = [d for d in addresses if d["name"] == "ADDRESS"]
pprint(addresses)
#  [{"comment": "",
#    "name": "ADDRESS",
#    "subnet": "127.0.0.100 255.255.255.252",
#    "uuid": "a386e4b0-d6cb-51ec-1e28-01e0bc0de43c",
#    ...
#    }]

print("\nUpdate address data in the Fortigate")
data = dict(subnet="127.0.0.255 255.255.255.255")
response = fgt.put(url="api/v2/cmdb/firewall/address/ADDRESS", data=data)
print("put", response)  # put <Response [200]>
addresses = fgt.get(url="api/v2/cmdb/firewall/address/")
addresses = [d for d in addresses if d["name"] == "ADDRESS"]
print(addresses[0]["subnet"])  # 127.0.0.255 255.255.255.255

print("\nChecks for presence of address in the Fortigate")
response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
print("exist", response)  # <Response [200]>

print("\nDeletes address from Fortigate")
response = fgt.delete(url="api/v2/cmdb/firewall/address/ADDRESS")
print("delete", response)  # <Response [200]>

print("\nChecks for absence of address in the Fortigate")
response = fgt.exist(url="api/v2/cmdb/firewall/address/ADDRESS")
print("exist", response)  # <Response [404]>

fgt.logout()
