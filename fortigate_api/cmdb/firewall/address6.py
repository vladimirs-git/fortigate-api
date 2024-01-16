"""Cmdb/firewall/address6 connector."""

from fortigate_api.connector import Connector


class Address6FC(Connector):
    """Cmdb/firewall/address6 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/address6"
