"""Cmdb/firewall/multicast-policy connector."""

from fortigate_api.connector import Connector


class MulticastPolicyFC(Connector):
    """Cmdb/firewall/multicast-policy connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/multicast-policy"
