"""Cmdb/router/auth-path connector."""

from fortigate_api.connector import Connector


class AuthPathRC(Connector):
    """Cmdb/router/auth-path connector."""

    uid = "name"
    _path = "api/v2/cmdb/router/auth-path"
