"""Cmdb/firewall/traffic-class connector."""

from fortigate_api.connector import Connector


class TrafficClassFC(Connector):
    """Cmdb/firewall/traffic-class connector."""

    uid = "class-id"
    _path = "api/v2/cmdb/firewall/traffic-class"
