"""Cmdb/application/group connector."""

from fortigate_api.connector import Connector


class GroupAC(Connector):
    """Cmdb/application/group connector."""

    uid = "name"
    _path = "api/v2/cmdb/application/group"
