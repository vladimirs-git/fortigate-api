"""Cmdb/web-proxy/global connector."""

from fortigate_api.connector import Connector


class GlobalWpC(Connector):
    """Cmdb/web-proxy/global connector."""

    uid = ""
    _path = "api/v2/cmdb/web-proxy/global"
