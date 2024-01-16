"""Cmdb/firewall/internet-service-extension connector."""

from fortigate_api.connector import Connector


class InternetServiceExtensionFC(Connector):
    """Cmdb/firewall/internet-service-extension connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-extension"
