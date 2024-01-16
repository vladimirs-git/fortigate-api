"""Cmdb/system.replacemsg/ftp connector."""

from fortigate_api.connector import Connector


class FtpSrC(Connector):
    """Cmdb/system.replacemsg/ftp connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/ftp"
