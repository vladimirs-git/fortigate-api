"""Cmdb/switch-controller/managed-switch connector."""

from fortigate_api.connector import Connector


class ManagedSwitchScC(Connector):
    """Cmdb/switch-controller/managed-switch connector."""

    uid = "switch-id"
    _path = "api/v2/cmdb/switch-controller/managed-switch"
