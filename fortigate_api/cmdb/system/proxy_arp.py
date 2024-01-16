"""Cmdb/system/proxy-arp connector."""

from fortigate_api.connector import Connector


class ProxyArpSC(Connector):
    """Cmdb/system/proxy-arp connector."""

    uid = "id"
    _path = "api/v2/cmdb/system/proxy-arp"
