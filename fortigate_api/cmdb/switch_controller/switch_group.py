"""Cmdb/switch-controller/switch-group connector."""

from fortigate_api.connector import Connector


class SwitchGroupScC(Connector):
    """Cmdb/switch-controller/switch-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller/switch-group"
