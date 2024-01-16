"""Cmdb/system/sit-tunnel connector."""

from fortigate_api.connector import Connector


class SitTunnelSC(Connector):
    """Cmdb/system/sit-tunnel connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/sit-tunnel"
