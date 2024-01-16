"""Cmdb/firewall/internet-service-custom connector."""

from fortigate_api.connector import Connector


class InternetServiceCustomFC(Connector):
    """Cmdb/firewall/internet-service-custom connector."""

    uid = "name"
    _path = "api/v2/cmdb/firewall/internet-service-custom"
