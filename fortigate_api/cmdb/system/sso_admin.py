"""Cmdb/system/sso-admin connector."""

from fortigate_api.connector import Connector


class SsoAdminSC(Connector):
    """Cmdb/system/sso-admin connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/sso-admin"
