"""Cmdb/web-proxy/wisp connector."""

from fortigate_api.connector import Connector


class WispWpC(Connector):
    """Cmdb/web-proxy/wisp connector."""

    uid = "name"
    _path = "api/v2/cmdb/web-proxy/wisp"
