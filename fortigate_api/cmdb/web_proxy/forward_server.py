"""Cmdb/web-proxy/forward-server connector."""

from fortigate_api.connector import Connector


class ForwardServerWpC(Connector):
    """Cmdb/web-proxy/forward-server connector."""

    uid = "name"
    _path = "api/v2/cmdb/web-proxy/forward-server"
