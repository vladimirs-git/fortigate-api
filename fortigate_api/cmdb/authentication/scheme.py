"""Cmdb/authentication/scheme connector."""

from fortigate_api.connector import Connector


class SchemeAC(Connector):
    """Cmdb/authentication/scheme connector."""

    uid = "name"
    _path = "api/v2/cmdb/authentication/scheme"
