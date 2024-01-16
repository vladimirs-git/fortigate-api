"""Cmdb/system/stp connector."""

from fortigate_api.connector import Connector


class StpSC(Connector):
    """Cmdb/system/stp connector."""

    uid = ""
    _path = "api/v2/cmdb/system/stp"
