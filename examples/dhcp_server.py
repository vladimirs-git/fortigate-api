"""DhcpServer examples."""

from pprint import pprint

from fortigate_api import FortigateAPI

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
fgt.login()

print("\nCreates dhcp server")
data = {
    "default-gateway": "192.168.255.1",
    "netmask": "255.255.255.0",
    "interface": "vlan.123",
    "ip-range": [{"start-ip": "192.168.255.2", "end-ip": "192.168.255.254", }],
}
response = fgt.dhcp_server.create(data=data)
print("dhcp_server.create", response)  # dhcp_server.create <Response [200]>

print("\nGets all dhcp_server")
dhcp_servers = fgt.dhcp_server.get()
print(f"dhcp_servers count={len(dhcp_servers)}")  # dhcp_server count=3

print("\nFilters dhcp_server by id (unique identifier)")
dhcp_servers = fgt.dhcp_server.get(uid="1")
pprint(dhcp_servers)
#  [{"id": 3,
#   "interface": "vlan.123",
#   "ip-mode": "range",
#   "ip-range": [{"end-ip": "192.168.255.254",
#                 "id": 1,
#                 "q_origin_key": 1,
#                 "start-ip": "192.168.255.2"}],
#    ...
#    }]

print("\nFilters dhcp_server by operator equals \"==\"")
dhcp_servers = fgt.dhcp_server.get(filter="interface==vlan.123")
print(f"dhcp_servers count={len(dhcp_servers)}")  # dhcp_server count=1

print("\nFilters dhcp_server by operator contains \"=@\"")
dhcp_servers = fgt.dhcp_server.get(filter="interface=@vlan.")
print(f"dhcp_servers count={len(dhcp_servers)}")  # dhcp_server count=1

print("\nFilters dhcp_server by operator not equals \"!=\"")
dhcp_servers = fgt.dhcp_server.get(filter="interface!=vlan.123")
print(f"dhcp_servers count={len(dhcp_servers)}")  # dhcp_server count=2

print("\nFilters dhcp_server by multiple conditions")
dhcp_servers = fgt.dhcp_server.get(filter=["default-gateway==192.168.255.1", "interface=@vlan."])
print(f"dhcp_servers count={len(dhcp_servers)}")  # dhcp_server count=1

print("\nUpdates dhcp_server data in the Fortigate")
data = {"dns-server1": "10.0.0.1"}
response = fgt.dhcp_server.update(uid="1", data=data)
print("dhcp_server.update", response, response.ok)  # dhcp_server.update <Response [200]> True

print("\nChecks for presence of dhcp_server in the Fortigate")
response = fgt.dhcp_server.is_exist(uid="1")
print("dhcp_server.is_exist", response)  # dhcp_server.is_exist True

print("\nDeletes dhcp_server from the Fortigate by name")
response = fgt.dhcp_server.delete(uid="1")
print("dhcp_server.delete", response, response.ok)  # dhcp_server.delete <Response [200]> True

print("\nDeletes dhcp_server from the Fortigate by filter")
response = fgt.dhcp_server.delete(filter="interface==vlan.123")
print("dhcp_server.delete", response, response.ok)  # dhcp_server.delete <Response [200]> True

fgt.logout()
