"""Cmdb/application/name connector."""

from fortigate_api.connector import Connector


class NameAC(Connector):
    """Cmdb/application/name connector."""

    uid = "name"
    _path = "api/v2/cmdb/application/name"
