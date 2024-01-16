"""Cmdb/system/email-server connector."""

from fortigate_api.connector import Connector


class EmailServerSC(Connector):
    """Cmdb/system/email-server connector."""

    uid = ""
    _path = "api/v2/cmdb/system/email-server"
