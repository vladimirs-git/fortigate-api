"""Cmdb/firewall/vip46 connector."""

from fortigate_api.connector import Connector


class Vip46FC(Connector):
    """Cmdb/firewall/vip46 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/vip46"
