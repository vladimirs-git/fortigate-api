"""Cmdb/firewall/ssl-ssh-profile connector."""

from fortigate_api.connector import Connector


class SslSshProfileFC(Connector):
    """Cmdb/firewall/ssl-ssh-profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/ssl-ssh-profile"
