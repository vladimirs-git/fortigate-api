"""Cmdb/firewall/proxy-address connector."""

from fortigate_api.connector import Connector


class ProxyAddressFC(Connector):
    """Cmdb/firewall/proxy-address connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/proxy-address"
