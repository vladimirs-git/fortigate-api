"""IP-Pool examples."""

from pprint import pprint

from fortigate_api import FortigateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
fgt.login()

print("\nGets all ip-pool in vdom \"root\" from the Fortigate")
ip_pools = fgt.ip_pool.get()
pprint(ip_pools)
# [{'arp-intf': '',
#   'arp-reply': 'enable',
#   'associated-interface': '',
#   'block-size': 128,
#   'comments': '',
#   'endip': '10.0.0.1',
#   'name': 'NAT-Source-01',
#   'num-blocks-per-user': 8,
#   'pba-timeout': 30,
#   'permit-any-host': 'disable',
#   'q_origin_key': 'NAT-Source-01',
#   'source-endip': '0.0.0.0',
#   'source-startip': '0.0.0.0',
#   'startip': '10.0.0.1',
#   'type': 'overload'},
# ...


print("\nGets filtered ip_pools by name (unique identifier)")
ip_pools = fgt.ip_pool.get(uid="NAT-Source-01")
pprint(ip_pools)
#  [{'arp-intf': '',
#   'arp-reply': 'enable',
#   'associated-interface': '',
#   'block-size': 128,
#   'comments': '',
#   'endip': '10.0.0.1',
#   'name': 'NAT-Source-01',
#   'num-blocks-per-user': 8,
#   'pba-timeout': 30,
#   'permit-any-host': 'disable',
#   'q_origin_key': 'NAT-Source-01',
#   'source-endip': '0.0.0.0',
#   'source-startip': '0.0.0.0',
#   'startip': '10.0.0.1',
#   'type': 'overload'}]

print("\nFilters ip_pools by operator equals \"==\"")
ip_pools = fgt.ip_pool.get(filter="name==NAT-Source-01")
print(f"ip_pools count={len(ip_pools)}")  # ip_pools count=1

print("\nFilters ip_pools by operator contains \"=@\"")
ip_pools = fgt.ip_pool.get(filter="name=@NAT-")
print(f"ip_pools count={len(ip_pools)}")  # ip_pools count=5

print("\nFilters ip_pools by multiple conditions")
ip_pools = fgt.ip_pool.get(filter=["name=@NAT-", "endip=@10.0.0."])
print(f"ip_pools count={len(ip_pools)}")  # ip_pools count=2

print("\nUpdates ip_pool data in the Fortigate")
data = dict(name="NAT-Source-01", comments="description")
response = fgt.ip_pool.update(uid="NAT-Source-01", data=data)
print("ip_pool.update", response)  # ip_pool.update <Response [200]>

print("\nChecks for presence of ip_pool in the Fortigate")
response = fgt.ip_pool.is_exist(uid="NAT-Source-01")
print("ip_pool.is_exist", response)  # ip_pool.is_exist True

fgt.logout()
