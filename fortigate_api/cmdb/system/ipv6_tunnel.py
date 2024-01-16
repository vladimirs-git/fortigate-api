"""Cmdb/system/ipv6-tunnel connector."""

from fortigate_api.connector import Connector


class Ipv6TunnelSC(Connector):
    """Cmdb/system/ipv6-tunnel connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/ipv6-tunnel"
