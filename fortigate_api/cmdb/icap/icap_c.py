"""Cmdb/icap connectors."""

from fortigate_api.cmdb.icap.profile import ProfileIC
from fortigate_api.cmdb.icap.server import ServerIC
from fortigate_api.fortigate import FortiGate


class IcapC:
    """Cmdb/icap connectors."""

    def __init__(self, fortigate: FortiGate, **kwargs):
        """Init IcapC."""

        self.profile = ProfileIC(fortigate, **kwargs)
        """:py:class:`.ProfileIC` cmdb/icap/profile."""

        self.server = ServerIC(fortigate, **kwargs)
        """:py:class:`.ServerIC` cmdb/icap/server."""
