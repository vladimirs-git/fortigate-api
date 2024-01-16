"""Cmdb/ips/global connector."""

from fortigate_api.connector import Connector


class GlobalIC(Connector):
    """Cmdb/ips/global connector."""

    uid = ""
    _path = "api/v2/cmdb/ips/global"
