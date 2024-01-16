"""Cmdb/system/mobile-tunnel connector."""

from fortigate_api.connector import Connector


class MobileTunnelSC(Connector):
    """Cmdb/system/mobile-tunnel connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/mobile-tunnel"
