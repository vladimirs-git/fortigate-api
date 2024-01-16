"""Cmdb/system/dns-server connector."""

from fortigate_api.connector import Connector


class DnsServerSC(Connector):
    """Cmdb/system/dns-server connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/dns-server"
