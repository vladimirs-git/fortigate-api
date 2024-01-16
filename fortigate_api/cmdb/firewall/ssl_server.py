"""Cmdb/firewall/ssl-server connector."""

from fortigate_api.connector import Connector


class SslServerFC(Connector):
    """Cmdb/firewall/ssl-server connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/ssl-server"
