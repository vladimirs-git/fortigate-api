"""Cmdb/firewall/multicast-address6 connector."""

from fortigate_api.connector import Connector


class MulticastAddress6FC(Connector):
    """Cmdb/firewall/multicast-address6 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/multicast-address6"
