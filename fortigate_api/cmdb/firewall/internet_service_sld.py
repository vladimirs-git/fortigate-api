"""Cmdb/firewall/internet-service-sld connector."""

from fortigate_api.connector import Connector


class InternetServiceSldFC(Connector):
    """Cmdb/firewall/internet-service-sld connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-sld"
