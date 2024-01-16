"""Cmdb/web-proxy/profile connector."""

from fortigate_api.connector import Connector


class ProfileWpC(Connector):
    """Cmdb/web-proxy/profile connector."""

    uid = "name"
    _path = "api/v2/cmdb/web-proxy/profile"
