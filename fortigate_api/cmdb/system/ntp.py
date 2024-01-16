"""Cmdb/system/ntp connector."""

from fortigate_api.connector import Connector


class NtpSC(Connector):
    """Cmdb/system/ntp connector."""

    uid = ""
    _path = "api/v2/cmdb/system/ntp"
