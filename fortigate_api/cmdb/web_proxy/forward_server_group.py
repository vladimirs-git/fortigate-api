"""Cmdb/web-proxy/forward-server-group connector."""

from fortigate_api.connector import Connector


class ForwardServerGroupWpC(Connector):
    """Cmdb/web-proxy/forward-server-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/web-proxy/forward-server-group"
