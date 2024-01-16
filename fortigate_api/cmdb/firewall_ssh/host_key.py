"""Cmdb/firewall.ssh/host-key connector."""

from fortigate_api.connector import Connector


class HostKeyFsC(Connector):
    """Cmdb/firewall.ssh/host-key connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall.ssh/host-key"
