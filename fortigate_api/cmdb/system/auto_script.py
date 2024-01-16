"""Cmdb/system/auto-script connector."""

from fortigate_api.connector import Connector


class AutoScriptSC(Connector):
    """Cmdb/system/auto-script connector."""

    uid = "name"
    _path = "api/v2/cmdb/system/auto-script"
