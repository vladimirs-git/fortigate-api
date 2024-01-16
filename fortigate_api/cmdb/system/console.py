"""Cmdb/system/console connector."""

from fortigate_api.connector import Connector


class ConsoleSC(Connector):
    """Cmdb/system/console connector."""

    uid = ""
    _path = "api/v2/cmdb/system/console"
