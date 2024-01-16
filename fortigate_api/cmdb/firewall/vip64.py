"""Cmdb/firewall/vip64 connector."""

from fortigate_api.connector import Connector


class Vip64FC(Connector):
    """Cmdb/firewall/vip64 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/vip64"
