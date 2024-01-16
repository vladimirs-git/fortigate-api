"""Cmdb/switch-controller/port-policy connector."""

from fortigate_api.connector import Connector


class PortPolicyScC(Connector):
    """Cmdb/switch-controller/port-policy connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller/port-policy"
