"""Cmdb/firewall/multicast-address connector."""

from fortigate_api.connector import Connector


class MulticastAddressFC(Connector):
    """Cmdb/firewall/multicast-address connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/multicast-address"
