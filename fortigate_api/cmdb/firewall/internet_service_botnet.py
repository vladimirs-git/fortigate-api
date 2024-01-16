"""Cmdb/firewall/internet-service-botnet connector."""

from fortigate_api.connector import Connector


class InternetServiceBotnetFC(Connector):
    """Cmdb/firewall/internet-service-botnet connector."""

    uid = "id"
    _path = "api/v2/cmdb/firewall/internet-service-botnet"
