"""Cmdb/firewall/internet-service-definition connector."""

from fortigate_api.connector import Connector


class InternetServiceDefinitionFC(Connector):
    """Cmdb/firewall/internet-service-definition connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-definition"
