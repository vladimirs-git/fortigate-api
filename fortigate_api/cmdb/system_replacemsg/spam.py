"""Cmdb/system.replacemsg/spam connector."""

from fortigate_api.connector import Connector


class SpamSrC(Connector):
    """Cmdb/system.replacemsg/spam connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/spam"
