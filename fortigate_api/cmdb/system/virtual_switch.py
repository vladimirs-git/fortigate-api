"""Cmdb/system/virtual-switch connector."""

from fortigate_api.connector import Connector


class VirtualSwitchSC(Connector):
    """Cmdb/system/virtual-switch connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/virtual-switch"
