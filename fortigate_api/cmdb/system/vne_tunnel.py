"""Cmdb/system/vne-tunnel connector."""

from fortigate_api.connector import Connector


class VneTunnelSC(Connector):
    """Cmdb/system/vne-tunnel connector."""

    uid = ""
    _path = "api/v2/cmdb/system/vne-tunnel"
