"""Cmdb/firewall/multicast-policy6 connector."""

from fortigate_api.connector import Connector


class MulticastPolicy6FC(Connector):
    """Cmdb/firewall/multicast-policy6 connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/multicast-policy6"
