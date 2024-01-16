"""Cmdb/firewall/internet-service-group connector."""

from fortigate_api.connector import Connector


class InternetServiceGroupFC(Connector):
    """Cmdb/firewall/internet-service-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/internet-service-group"
