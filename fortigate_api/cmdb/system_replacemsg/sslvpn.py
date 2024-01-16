"""Cmdb/system.replacemsg/sslvpn connector."""

from fortigate_api.connector import Connector


class SslvpnSrC(Connector):
    """Cmdb/system.replacemsg/sslvpn connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/sslvpn"
