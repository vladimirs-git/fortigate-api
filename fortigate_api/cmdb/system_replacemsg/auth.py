"""Cmdb/system.replacemsg/auth connector."""

from fortigate_api.connector import Connector


class AuthSrC(Connector):
    """Cmdb/system.replacemsg/auth connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/auth"
