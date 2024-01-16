"""Cmdb/web-proxy/debug-url connector."""

from fortigate_api.connector import Connector


class DebugUrlWpC(Connector):
    """Cmdb/web-proxy/debug-url connector."""

    uid = "name"
    _path = "api/v2/cmdb/web-proxy/debug-url"
