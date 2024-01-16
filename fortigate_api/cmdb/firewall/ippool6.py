"""Cmdb/firewall/ippool6 connector."""

from fortigate_api.connector import Connector


class Ippool6FC(Connector):
    """Cmdb/firewall/ippool6 connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/ippool6"
