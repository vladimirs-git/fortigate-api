"""Cmdb/firewall/internet-service-addition connector."""

from fortigate_api.connector import Connector


class InternetServiceAdditionFC(Connector):
    """Cmdb/firewall/internet-service-addition connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-addition"
