"""Cmdb/system/pppoe-interface connector."""

from fortigate_api.connector import Connector


class PppoeInterfaceSC(Connector):
    """Cmdb/system/pppoe-interface connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/pppoe-interface"
