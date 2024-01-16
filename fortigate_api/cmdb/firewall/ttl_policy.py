"""Cmdb/firewall/ttl-policy connector."""

from fortigate_api.connector import Connector


class TtlPolicyFC(Connector):
    """Cmdb/firewall/ttl-policy connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/ttl-policy"
