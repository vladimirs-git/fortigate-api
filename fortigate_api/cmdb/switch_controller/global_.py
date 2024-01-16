"""Cmdb/switch-controller/global connector."""

from fortigate_api.connector import Connector


class GlobalScC(Connector):
    """Cmdb/switch-controller/global connector."""

    uid = ""
    _path = "api/v2/cmdb/switch-controller/global"
