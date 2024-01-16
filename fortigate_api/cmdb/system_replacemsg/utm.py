"""Cmdb/system.replacemsg/utm connector."""

from fortigate_api.connector import Connector


class UtmSrC(Connector):
    """Cmdb/system.replacemsg/utm connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/utm"
