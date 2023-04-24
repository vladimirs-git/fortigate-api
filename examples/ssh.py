"""SSH examples.

- Show interface config
- Change interface description from "dmz" to "DMZ"
- Check interface description is changed
- Change read-timeout timer for long awaited commands
"""

import logging

from fortigate_api import FortigateAPI

logging.getLogger().setLevel(logging.DEBUG)

HOST = "host"
USERNAME = "username"
PASSWORD = "password"

fgt_api = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)
fgt_api.ssh.login()

# Show interface config
config = fgt_api.ssh.send_command("show system interface dmz")
print(config)
print()
# config system interface
#     edit "dmz"
#         set vdom "root"
#         set mode dhcp
#         set allowaccess ping https fgfm fabric
#         set status down
#         set type physical
#         set description "dmz"
#         set role dmz
#         set snmp-index 1
#     next
# end

# Change interface description from "dmz" to "DMZ"
cmds = ["config system interface",
        "edit dmz",
        "set description DMZ",
        "end"]
output = fgt_api.ssh.send_config_set(cmds)
print(output)
print()
# config system interface
# host (interface) # edit dmz
# host (dmz) # set description DMZ
# host (dmz) # end
# host #


# Check interface description is changed
config = fgt_api.ssh.send_command("show system interface dmz")
print(config)
print()
# config system interface
#     edit "dmz"
#         set vdom "root"
#         set mode dhcp
#         set allowaccess ping https fgfm fabric
#         set status down
#         set type physical
#         set description "DMZ"
#         set role dmz
#         set snmp-index 1
#     next
# end


# Change read-timeout timer for long awaited commands
cmds = ["execute ping-options repeat-count 2",
        "execute ping-options interval 30",
        "execute ping 8.8.8.8"]
# noinspection PyBroadException
try:
    _ = fgt_api.ssh.send_config_set(cmds)
except Exception:
    print("no answer for a long time, session timed out")
print()
# no answer for a long time, session timed out

ssh_params = dict(read_timeout_override=180)
fgt_api = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD, ssh=ssh_params)
output = fgt_api.ssh.send_config_set(cmds)
print(output)
# execute ping-options repeat-count 2
#
# host # execute ping-options interval 30
#
# host # execute ping 8.8.8.8
# PING 8.8.8.8 (8.8.8.8): 56 data bytes
# 64 bytes from 8.8.8.8: icmp_seq=0 ttl=61 time=10.3 ms
# 64 bytes from 8.8.8.8: icmp_seq=1 ttl=61 time=10.2 ms
#
# --- 8.8.8.8 ping statistics ---
# 2 packets transmitted, 2 packets received, 0% packet loss
# round-trip min/avg/max = 10.2/10.2/10.3 ms
#
# host #
