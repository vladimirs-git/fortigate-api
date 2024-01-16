"""Cmdb/firewall/internet-service-name connector."""

from fortigate_api.connector import Connector


class InternetServiceNameFC(Connector):
    """Cmdb/firewall/internet-service-name connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/internet-service-name"
