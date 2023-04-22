"""SSH examples for working with vdom.

- Get system arp from interfaces associated with vdom="VDOM"
- Get system arp from interfaces associated with vdom="root"
"""

from fortigate_api import FortigateAPI

HOST = "hostname"
USERNAME = "username"
PASSWORD = "password"
VDOM = "VDOM"

# Fortigate with configured VDOMs. diagnostic commands for custom vdom
fgt_vdom = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
vdom_commands = ["config vdom", f"edit {VDOM}"]
output = fgt_vdom.ssh.send_config_set(vdom_commands)
print(output)
# config vdom
#
# hostname (vdom) # edit VDOM
# current vf=VDOM:1
#
# hostname (VDOM) #

output = fgt_vdom.ssh.send_command("get system arp")
print(output)
# hostname (VDOM) #
# Address           Age(min)   Hardware Addr      Interface
# 10.0.1.1          0          00:00:00:00:00:71 v1000
# 10.0.4.1          0          00:00:00:00:00:71 v4000

# Fortigate with configured VDOMs. diagnostic commands for vdom=root
fgt_root = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
vdom_commands = ["config vdom", "edit root"]
output = fgt_root.ssh.send_config_set(vdom_commands)
print(output)
# config vdom
#
# hostname (vdom) # edit root
# current vf=root:0
#
# hostname (root) #

output = fgt_root.ssh.send_command("get system arp")
print(output)
# hostname (root) #
# Address           Age(min)   Hardware Addr      Interface
# 10.0.5.1          7          00:00:00:00:00:71 v5000
