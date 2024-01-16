"""Cmdb/firewall/internet-service connector."""

from fortigate_api.connector import Connector


class InternetServiceFC(Connector):
    """Cmdb/firewall/internet-service connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service"
    _path_ui = "ng/firewall/internet_service"
