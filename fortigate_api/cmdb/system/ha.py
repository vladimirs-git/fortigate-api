"""Cmdb/system/ha connector."""

from fortigate_api.connector import Connector


class HaSC(Connector):
    """Cmdb/system/ha connector."""

    uid = ""
    _path = "api/v2/cmdb/system/ha"
