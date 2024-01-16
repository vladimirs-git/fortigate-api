"""Cmdb/firewall/internet-service-owner connector."""

from fortigate_api.connector import Connector


class InternetServiceOwnerFC(Connector):
    """Cmdb/firewall/internet-service-owner connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-owner"
