"""Cmdb/firewall/shaping-policy connector."""

from fortigate_api.connector import Connector


class ShapingPolicyFC(Connector):
    """Cmdb/firewall/shaping-policy connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/shaping-policy"
