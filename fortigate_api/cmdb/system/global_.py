"""Cmdb/system/global connector."""

from fortigate_api.connector import Connector


class GlobalSC(Connector):
    """Cmdb/system/global connector."""

    uid = ""
    _path = "api/v2/cmdb/system/global"
    _path_ui = "/ng/system/settings"
