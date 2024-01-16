"""Cmdb/system/lte-modem connector."""

from fortigate_api.connector import Connector


class LteModemSC(Connector):
    """Cmdb/system/lte-modem connector."""

    uid = ""
    _path = "api/v2/cmdb/system/lte-modem"
