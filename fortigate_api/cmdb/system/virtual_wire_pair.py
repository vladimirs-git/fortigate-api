"""Cmdb/system/virtual-wire-pair connector."""

from fortigate_api.connector import Connector


class VirtualWirePairSC(Connector):
    """Cmdb/system/virtual-wire-pair connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/virtual-wire-pair"
