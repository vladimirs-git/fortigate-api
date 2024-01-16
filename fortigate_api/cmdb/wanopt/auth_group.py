"""Cmdb/wanopt/auth-group connector."""

from fortigate_api.connector import Connector


class AuthGroupWC(Connector):
    """Cmdb/wanopt/auth-group connector."""

    uid = "name"
    _path = "api/v2/cmdb/wanopt/auth-group"
