"""Cmdb/user/group connector."""

from fortigate_api.connector import Connector


class GroupUC(Connector):
    """Cmdb/user/group connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/group"
