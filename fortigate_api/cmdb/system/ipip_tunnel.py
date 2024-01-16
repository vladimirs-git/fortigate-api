"""Cmdb/system/ipip-tunnel connector."""

from fortigate_api.connector import Connector


class IpipTunnelSC(Connector):
    """Cmdb/system/ipip-tunnel connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/ipip-tunnel"
