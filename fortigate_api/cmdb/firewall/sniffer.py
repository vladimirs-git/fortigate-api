"""Cmdb/firewall/sniffer connector."""

from fortigate_api.connector import Connector


class SnifferFC(Connector):
    """Cmdb/firewall/sniffer connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/sniffer"
