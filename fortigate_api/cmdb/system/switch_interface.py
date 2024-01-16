"""Cmdb/system/switch-interface connector."""

from fortigate_api.connector import Connector


class SwitchInterfaceSC(Connector):
    """Cmdb/system/switch-interface connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/switch-interface"
