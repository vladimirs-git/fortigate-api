"""Cmdb/system.dhcp connectors."""

from fortigate_api.cmdb.system_dhcp.server import ServerSdC
from fortigate_api.fortigate import FortiGate


class SystemDhcpC:
    """Cmdb/system.dhcp connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SystemDhcpC."""
        self.server = ServerSdC(fortigate, **kwargs)
        """:py:class:`.ServerSdC` cmdb/system.dhcp/server."""
