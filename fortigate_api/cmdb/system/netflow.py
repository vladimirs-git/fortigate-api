"""Cmdb/system/netflow connector."""

from fortigate_api.connector import Connector


class NetflowSC(Connector):
    """Cmdb/system/netflow connector."""

    uid = ""
    _path = "api/v2/cmdb/system/netflow"
