"""Cmdb/system.replacemsg/mail connector."""

from fortigate_api.connector import Connector


class MailSrC(Connector):
    """Cmdb/system.replacemsg/mail connector."""

    uid = "msg-type"
    _path = "api/v2/cmdb/system.replacemsg/mail"
