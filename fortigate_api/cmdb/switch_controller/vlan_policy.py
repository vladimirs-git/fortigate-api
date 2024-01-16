"""Cmdb/switch-controller/vlan-policy connector."""

from fortigate_api.connector import Connector


class VlanPolicyScC(Connector):
    """Cmdb/switch-controller/vlan-policy connector."""

    uid = "name"
    _path = "api/v2/cmdb/switch-controller/vlan-policy"
