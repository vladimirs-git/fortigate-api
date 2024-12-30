"""Cmdb/system.dhcp6 connectors."""

from fortigate_api.cmdb.system_dhcp6.server import ServerSdC
from fortigate_api.fortigate import FortiGate


class SystemDhcp6C:
    """Cmdb/system.dhcp6 connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init SystemDhcp6C."""
        self.server = ServerSdC(fortigate, **kwargs)
        """:py:class:`.ServerSdC` cmdb/system.dhcp6/server."""
