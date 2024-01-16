"""Cmdb/system/ptp connector."""

from fortigate_api.connector import Connector


class PtpSC(Connector):
    """Cmdb/system/ptp connector."""

    uid = ""
    _path = "api/v2/cmdb/system/ptp"
