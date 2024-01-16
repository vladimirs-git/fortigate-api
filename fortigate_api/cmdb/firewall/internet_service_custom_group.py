"""Cmdb/firewall/internet-service-custom-group connector."""

from fortigate_api.connector import Connector


class InternetServiceCustomGroupFC(Connector):
    """Cmdb/firewall/internet-service-custom-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/internet-service-custom-group"
