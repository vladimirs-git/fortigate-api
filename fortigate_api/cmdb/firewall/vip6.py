"""Cmdb/firewall/vip6 connector."""

from fortigate_api.connector import Connector


class Vip6FC(Connector):
    """Cmdb/firewall/vip6 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/vip6"
