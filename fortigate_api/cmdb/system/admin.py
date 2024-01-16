"""Cmdb/system/admin connector."""

from fortigate_api.connector import Connector


class AdminSC(Connector):
    """Cmdb/system/admin connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/admin"
