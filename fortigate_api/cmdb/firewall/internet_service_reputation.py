"""Cmdb/firewall/internet-service-reputation connector."""

from fortigate_api.connector import Connector


class InternetServiceReputationFC(Connector):
    """Cmdb/firewall/internet-service-reputation connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-reputation"
