"""Cmdb/system/gre-tunnel connector."""

from fortigate_api.connector import Connector


class GreTunnelSC(Connector):
    """Cmdb/system/gre-tunnel connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/gre-tunnel"
