"""Cmdb/wireless-controller/global connector."""

from fortigate_api.connector import Connector


class GlobalWcC(Connector):
    """Cmdb/wireless-controller/global connector."""

    uid = ""
    _path = "api/v2/cmdb/wireless-controller/global"
