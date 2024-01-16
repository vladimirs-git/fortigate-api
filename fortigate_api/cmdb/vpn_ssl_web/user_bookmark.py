"""Cmdb/vpn.ssl.web/user-bookmark connector."""

from fortigate_api.connector import Connector


class UserBookmarkVswC(Connector):
    """Cmdb/vpn.ssl.web/user-bookmark connector."""

    uid = "name"
    _path = "api/v2/cmdb/vpn.ssl.web/user-bookmark"
