"""Cmdb/system.replacemsg/alertmail connector."""

from fortigate_api.connector import Connector


class AlertmailSrC(Connector):
    """Cmdb/system.replacemsg/alertmail connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/alertmail"
