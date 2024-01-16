"""Cmdb/firewall/auth-portal connector."""

from fortigate_api.connector import Connector


class AuthPortalFC(Connector):
    """Cmdb/firewall/auth-portal connector."""

    uid = ""
    _path = "api/v2/cmdb/firewall/auth-portal"
