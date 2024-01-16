"""Cmdb/system/modem connector."""

from fortigate_api.connector import Connector


class ModemSC(Connector):
    """Cmdb/system/modem connector."""

    uid = ""
    _path = "api/v2/cmdb/system/modem"
