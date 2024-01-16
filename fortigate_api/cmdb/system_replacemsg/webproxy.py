"""Cmdb/system.replacemsg/webproxy connector."""

from fortigate_api.connector import Connector


class WebproxySrC(Connector):
    """Cmdb/system.replacemsg/webproxy connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/webproxy"
