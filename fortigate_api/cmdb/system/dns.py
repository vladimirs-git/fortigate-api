"""Cmdb/system/dns connector."""

from fortigate_api.connector import Connector


class DnsSC(Connector):
    """Cmdb/system/dns connector."""

    uid = ""
    _path = "api/v2/cmdb/system/dns"
