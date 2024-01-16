"""Cmdb/firewall/internet-service-list connector."""

from fortigate_api.connector import Connector


class InternetServiceListFC(Connector):
    """Cmdb/firewall/internet-service-list connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-list"
