"""Cmdb/system.replacemsg/admin connector."""

from fortigate_api.connector import Connector


class AdminSrC(Connector):
    """Cmdb/system.replacemsg/admin connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/admin"
