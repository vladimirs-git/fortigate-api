"""Cmdb/system/vxlan connector."""

from fortigate_api.connector import Connector


class VxlanSC(Connector):
    """Cmdb/system/vxlan connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/vxlan"
