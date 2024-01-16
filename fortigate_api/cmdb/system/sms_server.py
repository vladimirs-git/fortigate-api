"""Cmdb/system/sms-server connector."""

from fortigate_api.connector import Connector


class SmsServerSC(Connector):
    """Cmdb/system/sms-server connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/sms-server"
