"""Cmdb/system.replacemsg/http connector."""

from fortigate_api.connector import Connector


class HttpSrC(Connector):
    """Cmdb/system.replacemsg/http connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/http"
