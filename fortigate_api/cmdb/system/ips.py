"""Cmdb/system/ips connector."""

from fortigate_api.connector import Connector


class IpsSC(Connector):
    """Cmdb/system/ips connector."""

    uid = ""
    _path = "api/v2/cmdb/system/ips"
